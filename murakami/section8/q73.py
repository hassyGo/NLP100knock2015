#!/usr/bin/env python
#coding: utf-8

"""
    73. 学習
    72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
    
    74. 予測
    73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
"""

from q71 import *
from q72 import *
import numpy as np
import math

def sigmoid(x):
    return 1.0 / (1 + math.exp(-1*x))

class LogisticRegulation:
    def __init__(self,dataList,learnRate,learnIter):
        print "logistic regulation init..."
        self.featureDim = len(dataList[0].feature)
        self.weightVec = np.zeros(self.featureDim)
        self.dataList = dataList
        self.learnRate = learnRate
        self.learnIter = learnIter

    def learning(self):
        print "logistic regulation learning..."
        for it in range(self.learnIter):
            for data in self.dataList:
                featureVec = data.feature
                t = 1.0
                if data.label == -1: t = 0.0
                dWeightVec = (t - sigmoid(np.dot(self.weightVec,featureVec))) * featureVec
                self.weightVec = self.weightVec + self.learnRate * dWeightVec
            #print self.weightVec
            self.learningCheck()

    def learningCheck(self):
        probAve = 0.0
        for data in self.dataList:
            featureVec = data.feature
            prob = sigmoid(np.dot(self.weightVec,featureVec))
            if data.label == -1: prob = 1 - prob
            #print data.label,prob
            probAve += prob

        probAve = probAve / len(self.dataList)
        print "avarage:", probAve


if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)

    logistic = LogisticRegulation(dataList,0.1,200)
    logistic.learning()

    #74
    logistic.learningCheck()