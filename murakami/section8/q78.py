#!/usr/bin/env python
#coding: utf-8

"""
    78. 5分割交差検定
    76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
"""

from q71 import *
from q72 import *
from q73 import *
import numpy as np
import math

class LogisticRegulationCrossValidation:
    def __init__(self,dataList,testDataList,learnRate,learnIter,th):
        print "logistic regulation init..."
        self.featureDim = len(dataList[0].feature)
        self.weightVec = np.zeros(self.featureDim)
        self.dataList = dataList
        self.testDataList = testDataList
        self.learnRate = learnRate
        self.learnIter = learnIter
        self.th = th
        
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
                
                dWeightVec = (t - sigmoid(np.dot(self.weightVec,featureVec))) * featureVec
                self.weightVec = self.weightVec + self.learnRate * dWeightVec

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
        for data in self.testDataList:
            featureVec = data.feature
            prob = sigmoid(np.dot(self.weightVec,featureVec))
            predictProb = prob
                
            #76
            predictLabel = +1
            if predictProb < self.th:
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

def split_list(list, n):
    l = len(list)
    size = l / n + (l % n > 0)
    return [ list[i:i+size] for i in range(0, l, size) ]

if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)
    
    K = 5
    dataListList = split_list(dataList,K)
    for i in range(K):
        print len(dataListList[i])
    
    logisticList = []
    
    for i in range(K):
        learnData = []
        testData = []
        for j in range(K):
            if i == j:
                testData = dataListList[j]
            else:
                learnData += dataListList[j]

        logistic = LogisticRegulationCrossValidation(learnData,testData,0.1,100,0.5)
        #logistic.learning()
        #logistic.outputWeightVec("weight%d.txt" % (i+1))
        logistic.readWeightVec("weight%d.txt" % (i+1))
        logistic.learningCheck(False)
        logisticList.append(logistic)

    allDataCount = 0
    allCorrectCount = 0
    allPositiveCount = 0
    allPositivePredictCount = 0
    allPositiveCorrectCount = 0
    for i in range(K):
        print logisticList[i].getResultDic()
        allDataCount += logisticList[i].getResultDic()["dataCount"]
        allCorrectCount += logisticList[i].getResultDic()["correctCount"]
        allPositiveCount += logisticList[i].getResultDic()["positiveCount"]
        allPositivePredictCount += logisticList[i].getResultDic()["positivePredictCount"]
        allPositiveCorrectCount += logisticList[i].getResultDic()["positiveCorrectCount"]

    correctRate = allCorrectCount * 1.0 / allDataCount
    precision = allPositiveCorrectCount * 1.0 / allPositivePredictCount
    recall = allPositiveCorrectCount * 1.0 / allPositiveCount
    f1 = 2 * precision * recall / (precision + recall)

    print "positive: P =",precision,"R =",recall,"F1 =",f1


