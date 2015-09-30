#!/usr/bin/env python
#coding: utf-8

"""
    72. 素性抽出
    極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

from q71 import *
from stemming.porter2 import stem
from collections import Counter
import numpy as np

#学習データのクラス
class LearnData:
    def __init__(self,feature,label):
        self.feature = feature
        self.label = label

    def show(self):
        print self.label,self.feature

#ファイルに出てくる単語のうち、出現頻度が10以上である単語のリストを取得する関数
def makeWordlist(filename,stopwordList):
    print "making wordlist from '" + filename + "'"
    f = open(filename)
    lines = f.readlines()
    
    stemWords = []
    for line in lines:
        words = line.split()[1:]
        stemWords.extend([stem(word) for word in words])
    counter = Counter(stemWords)

    wordlist = []
    for word,cnt in counter.most_common():
        if cnt >= 10 and (word in stopwordList) == False:
            #print word,cnt
            wordlist.append(word)
    return wordlist

#文から特徴ベクトルを生成する関数
def makeFeatures(sentence,dictionary):
    wordlist = dictionary["wordlist"]
    feature = []
    for word in wordlist:
        if word in sentence:
            feature.append(1)
        else:
            feature.append(0)
    return np.array(feature)

#ファイル中の各文から特徴ベクトルと正解ラベルを生成し、それらのペアを学習データとして、そのリストを返す関数
def makeData(filename,dictionary):
    print "making learning data from '" + filename + "'"
    dataList = []
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        label = int(line.split()[0])
        feature = makeFeatures(line.split()[1:],dictionary)
        data = LearnData(feature,label)
        dataList.append(data)
    return dataList


if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)

    for data in dataList[0:3]:
        data.show()