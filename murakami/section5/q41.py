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


class Chunk:
    def __init__(self,id,link):
        self.morphs = []
        self.dst = int(link)
        self.srcs = int(id)

    def pushMorph(self,m):
        self.morphs.append(m)
    
    #文節の文字列を返す
    def getText(self):
        return "".join([m.surface for m in self.morphs])

    #文節の情報を文字列で返す
    def getString(self):
        return "(string=%s,dst=%d)" % (self.getText() ,self.dst)

    #文節の中にPOSを含むものがあるならTrue
    def isIncludePos(self,pos):
        return pos in [m.pos.encode('utf-8') for m in self.morphs]


def printChunkList(list):
    print "[" + ",".join([c.getString() for c in list]) + "]"


def makeSentenceListFromXml(filename):
    root = readXml(filename)
    sentences = []
    for sIte in root:
        tmpSentence = []
        for cIte in sIte:
            c = Chunk(cIte.get("id"),cIte.get("link"))
            for mIte in cIte:
                m = Morph(mIte.get("feature"),mIte.text)
                c.pushMorph(m)
            tmpSentence.append(c)
        sentences.append(list(tmpSentence))
    return sentences

if __name__ == "__main__":
    sentences = makeSentenceListFromXml("neko.xml")
    
    printChunkList(sentences[7])