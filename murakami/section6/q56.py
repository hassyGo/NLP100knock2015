#!/usr/bin/env python
#coding: utf-8

"""
    56. 共参照解析
    Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""


from q53 import *


class Coreference: #Coreferenceクラス
    def __init__(self,sentenceId,start,end,head,text,isRepresentative):
        #int
        self.sentenceId = int(sentenceId)
        self.start = int(start)
        self.end = int(end)
        self.head = int(head)
        #string
        self.text = text
        #bool
        self.isRepresentative = bool(isRepresentative)

    def show(self):#デバッグ用
        print "Coreference : sentence=%d,start=%d,end=%d,head=%d,text=%s,isRepresentative=%d" % (self.sentenceId,self.start,self.end,self.head,self.text,self.isRepresentative)


def makeCoreferenceChains(root):
    coreferenceChains = []
    for coreference in root.iter("coreference"):#<coreference> ... </coreference>のノードを再帰的に探索してくれる
        coreferenceChain = []
        for mention in coreference:
            if mention.tag != "mention": break
            c = Coreference(mention.find("sentence").text,
                            mention.find("start").text,
                            mention.find("end").text,
                            mention.find("head").text,
                            mention.find("text").text,
                            mention.get("representative"))
            coreferenceChain.append(c)
        if len(coreferenceChain) > 0:
            coreferenceChains.append(coreferenceChain)
    return coreferenceChains


def getRepresentative(coreferenceChains,sentenceId,tokenId):
    for cc in coreferenceChains:
        for c in cc:
            if c.head == tokenId and c.sentenceId == sentenceId:
                return cc[0].text

    return ""


if __name__ == "__main__":
    root = readXml("nlp_sample.txt.xml") #xmlから木構造を作る
    
    coreferenceChains = makeCoreferenceChains(root)
   
    for sentences in root.iter("sentences"):
        for sentence in sentences.iter("sentence"):
            sentenceId = int(sentence.get("id"))
            for token in sentence.iter("token"):
                tokenId = int(token.get("id"))
                representative = getRepresentative(coreferenceChains,sentenceId,tokenId)
                if (representative != ""):
                    print "%s ( %s )" % (token.find("word").text,representative)
                else:
                    print token.find("word").text