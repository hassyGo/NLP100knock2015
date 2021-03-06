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
    
        self.dataCount = 0
        self.correctCount = 0
        self.positiveCount = 0
        self.positivePredictCount = 0
        self.positiveCorrectCount = 0
    
    def __init__(self,dataList,testDataList,learnRate,learnIter):
        print "logistic regulation init..."
        self.featureDim = len(dataList[0].feature)
        self.weightVec = np.zeros(self.featureDim)
        self.dataList = dataList
        self.learnRate = learnRate
        self.learnIter = learnIter
        
        self.dataCount = 0
        self.correctCount = 0
        self.positiveCount = 0
        self.positivePredictCount = 0
        self.positiveCorrectCount = 0

    def learning(self):
        print "logistic regulation learning..."
        for it in range(self.learnIter):
            for data in self.dataList:
                featureVec = data.feature
                t = 1.0
                if data.label == -1: t = 0.0
                
                #prob = sigmoid(np.dot(self.weightVec,featureVec))
                #if data.label == -1: prob = 1 - prob
                
                dWeightVec = (t - sigmoid(np.dot(self.weightVec,featureVec))) * featureVec
                self.weightVec = self.weightVec + self.learnRate * dWeightVec
            
                #prob2 = sigmoid(np.dot(self.weightVec,featureVec))
                #if data.label == -1: prob2 = 1 - prob2
            
            #print self.weightVec
            self.learningCheck(False)

    def outputWeightVec(self,filename):
        f = open(filename,"w")
        f.write(",".join([str(m) for m in self.weightVec]))
        f.close()
    
    def readWeightVec(self,filename):
        f = open(filename)
        self.weightVec = np.array([float(m) for m in f.readline().split(",")])

    def learningCheck(self,isShow):
        
        #77
        dataCount = 0
        correctCount = 0
        positiveCount = 0
        positivePredictCount = 0
        positiveCorrectCount = 0
        
        probAve = 0.0
        for data in self.dataList:
            featureVec = data.feature
            prob = sigmoid(np.dot(self.weightVec,featureVec))
            predictProb = prob
            
            #76
            predictLabel = +1
            if predictProb < 0.5:
                predictLabel = -1
                predictProb = 1 - predictProb
            if isShow:
                print "%s\t%s\t%s" % (data.label,predictLabel,predictProb)
            
            #77
            if data.label == predictLabel:
                correctCount += 1
            dataCount += 1
            if data.label == 1: positiveCount += 1
            if predictLabel == 1: positivePredictCount += 1
            if data.label == predictLabel and predictLabel == 1: positiveCorrectCount += 1
            
            
            if data.label == -1: prob = 1 - prob
            probAve += prob

        probAve = probAve / len(self.dataList)
        print "avarage:", probAve,self.learnRate
        print "correct rate : ",correctCount * 1.0 / dataCount

        #77
        precision = positiveCorrectCount * 1.0 / positivePredictCount
        recall = positiveCorrectCount * 1.0 / positiveCount
        f1 = 2 * precision * recall / (precision + recall)
        print "positive: P =",precision,"R =",recall,"F1 =",f1

        #78
        self.dataCount = dataCount
        self.correctCount = correctCount
        self.positiveCount = positiveCount
        self.positivePredictCount = positivePredictCount
        self.positiveCorrectCount = positiveCorrectCount

    def getResultDic(self):
        return {"dataCount":self.dataCount,"correctCount":self.correctCount,"positiveCount":self.positiveCount,"positivePredictCount":self.positivePredictCount,"positiveCorrectCount":self.positiveCorrectCount}


if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)

    #73
    logistic = LogisticRegulation(dataList,0.1,100)
    logistic.readWeightVec("weight.txt")
    logistic.learning()

    #74
    logistic.learningCheck(False)
    logistic.outputWeightVec("weight.txt")