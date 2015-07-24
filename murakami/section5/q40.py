#!/usr/bin/env python
#coding: utf-8

"""
    40. 係り受け解析結果の読み込み（形態素）
    形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""


import xml.etree.ElementTree as ET
import itertools


class Morph:
    def __init__(self,feature,text):
        list = feature.split(",")
        self.surface = text
        self.base = list[6]
        self.pos = list[0]
        self.pos1 = list[1]

    def getString(self):
        return "(surface=%s,base=%s,pos=%s,pos1=%s)" % (self.surface,self.base,self.pos,self.pos1)


def printMorphList(list):
    print "[" + ",".join([m.getString() for m in list]) + "]"


def readXml(filename):
    with open(filename) as f:
        it = itertools.chain('<root>', f, '</root>')#もしルートタグがない場合はつける
        root = ET.fromstringlist(it)
    return root


if __name__ == "__main__":
    root = readXml("neko.xml")


    sentences = []
    for sIte in root:
        tmpSentence = []
        for cIte in sIte:
            for mIte in cIte:
                m = Morph(mIte.get("feature"),mIte.text)
                tmpSentence.append(m)
        sentences.append(list(tmpSentence))

    printMorphList(sentences[2])

