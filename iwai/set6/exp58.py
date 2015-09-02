# !/usr/bin/python
# coding:UTF-8
# 6-(58):タプルの抽出
#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．
#述語: nsubj関係とdobj関係の子（dependant）を持つ単語
#主語: 述語からnsubj関係にある子（dependent）
#目的語: 述語からdobj関係にある子（dependent）

import re
import sys
import exp50
import exp57

def make_sentence(nsubj_pairs, dobj_pairs):
    sentences = []

    for nsubj in nsubj_pairs:
        sentence = []
        for dobj in dobj_pairs:
            if nsubj[0] == dobj[0]:
                sentence.append(dobj[1])
                sentence.append(nsubj)
        sentences.append(sentence)

    return sentences

def main():
    fw = open('58.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    collapsed_dependencies = exp57.make_collapsed_dependencies(document)

    flag = 0
    nsubj_pairs = []
    dobj_pairs = []
    
    for line in collapsed_dependencies[2]:
    #for line in collapsed_dependencies:
        search_nsubj = re.search('<dep type="nsubj">', line)
        search_dobj = re.search('<dep type="dobj">', line)
        
        if search_nsubj:
            flag = 1
            nsubj_pair = []
        if search_dobj:
            flag = 2
            dobj_pair = []
        if line == '</dep>':
            flag = 0
        if flag == 1:
            governor = exp57.search_governor(line)
            dependent = exp57.search_dependent(line)

            if governor != None:
                nsubj_pair.append(governor)
            if dependent != None:
                nsubj_pair.append(dependent)
                if len(nsubj_pair) == 2:
                    nsubj_pairs.append(nsubj_pair)
            
        if flag == 2:
            governor = exp57.search_governor(line)
            dependent = exp57.search_dependent(line)

            if governor != None:
                dobj_pair.append(governor)
            if dependent != None:
                dobj_pair.append(dependent)
                if len(dobj_pair) == 2:
                    dobj_pairs.append(dobj_pair)
            
    sentences = make_sentence(nsubj_pairs,dobj_pairs)
    #print sentences
    
    for sentence in sentences:
         if len(sentence) == 2:
             print sentence[1][1], sentence[1][0], sentence[0]
             
    fw.close()

    
if __name__ == "__main__":
    main()

    
