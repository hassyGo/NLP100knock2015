#!/usr/bin/env python
#coding: utf-8

"""
    41. 係り受け解析結果の読み込み（文節・係り受け）
    40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

#import q40
from q40 import *
import xml.etree.ElementTree as ET
import itertools
import re


class Chunk:
    def __init__(self,id,link,linked):
        self.morphs = [] #形態素列 list
        self.dst = int(link) #かかり先ID int
        self.id = int(id) #自分のID int
        self.srcs = linked #かかり元ID list

    def pushMorph(self,m):
        self.morphs.append(m)
    
    #文節の文字列を返す
    def getText(self):
        return "".join([m.surface for m in self.morphs if m.pos != u"記号"])
    
    #文節の名詞句を置き換えた文字列を返す(stringが空の時は置き換えない)
    def getNPReplaceText(self,string):
        if string == "":return self.getText()
        s = ""
        for m in self.morphs:
            if m.pos == u"記号":continue
            if m.pos == u"名詞":
                s += string
            else:
                s += m.surface
    
        s = re.sub(u'XX+','X',s)
        return s
    

    #文節の文字列とかかり先をstringで返す
    def getString(self):
        return "(string=%s,dst=%d)" % (self.getText() ,self.dst)
    
    #文節の情報すべてをstringで返す
    def getInfoString(self):
        linkedString = ",".join([str(i) for i in self.srcs])
        return "(id=%d,string=%s,dst=%d,srcs=" % (self.id ,self.getText() ,self.dst) + linkedString + ")"

    #文節の中にPOSを含むものがあるならTrue
    def isIncludePos(self,pos):
        return pos in [m.pos.encode('utf-8') for m in self.morphs]

    #文節の中のPOSと一致するindexのリストを返す
    def getPosIndices(self,pos):
        return [index for index in range(len(self.morphs)) if self.morphs[index].pos.encode('utf-8') == pos]

    #文節の中のPOS1と一致するindexのリストを返す
    def getPos1Indices(self,pos1):
        return [index for index in range(len(self.morphs)) if self.morphs[index].pos1.encode('utf-8') == pos1]


def printChunkList(list):
    print "[" + ",".join([c.getString() for c in list]) + "]"
#print "[" + ",".join([c.getInfoString() for c in list]) + "]"


def makeSentenceListFromXml(filename):
    root = readXml(filename)
    sentences = []
    for sIte in root:
        tmpSentence = []
        for cIte in sIte:
            linked = [int(m.get("id")) for m in sIte if m.get("link") == cIte.get("id")]
            c = Chunk(cIte.get("id"),cIte.get("link"),linked)
            for mIte in cIte:
                m = Morph(mIte.get("feature"),mIte.text)
                c.pushMorph(m)
            tmpSentence.append(c)
        sentences.append(list(tmpSentence))
    return sentences

if __name__ == "__main__":
    sentences = makeSentenceListFromXml("neko.xml")
    
    printChunkList(sentences[7])