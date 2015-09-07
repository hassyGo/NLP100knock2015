#!/usr/bin/env python
#coding: utf-8

"""
    58. タプルの抽出
    Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．
    
    述語: nsubj関係とdobj関係の子（dependant）を持つ単語
    主語: 述語からnsubj関係にある子（dependent）
    目的語: 述語からdobj関係にある子（dependent）
"""


from q53 import *



if __name__ == "__main__":
    root = readXml("nlp.txt.xml") #xmlから木構造を作る

    for sentences in root.iter("sentences"):
        for sentence in sentences.iter("sentence"):
            sentenceId = sentence.get("id")
            
            tokenDic = {}#tokenのIDをkeyとしてtokenのtextをvalueとする辞書を用意
            for token in sentence.iter("token"):
                tokenDic[token.get("id")] = token.find("word").text
            
            dependentDic = {}#かかり元をkeyとしてかかり先のリストをvalueとする辞書を作成
            
            
            for dependency in sentence.iter("dependencies"):
                if dependency.get("type") == "collapsed-dependencies":
                    for dep in dependency.iter("dep"):
                        type = dep.get("type")
                        gov = dep.find("governor").text
                        govId = dep.find("governor").get("idx")
                        dependent = dep.find("dependent").text
                        dependentId = dep.find("dependent").get("idx")

                        if govId in dependentDic:
                            dependentDic[govId].append((dependentId,type))
                        else:
                            dependentDic[govId] = [(dependentId,type)]

            for k,v in dependentDic.items():
                types = map(lambda n:n[1],v)#タプルのリストの２番目の要素のみのリスト
                if "nsubj" in types and "dobj" in types:
                    pred = tokenDic[k]
                    sub = tokenDic[v[types.index("nsubj")][0]]
                    obj = tokenDic[v[types.index("dobj")][0]]

                    print "\t".join([sub,pred,obj])

