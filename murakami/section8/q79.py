#!/usr/bin/env python
#coding: utf-8

"""
    79. 適合率-再現率グラフの描画
    ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
"""

from q71 import *
from q72 import *
from q73 import *
from q78 import *
import numpy as np
import math

import matplotlib.pyplot as plt



if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)
    
    K = 5
    dataListList = split_list(dataList,K)
    for i in range(K):
        print len(dataListList[i])
    
    results = []
    
    for r in range(1,100):
        th = r * 0.01

    
        logisticList = []
        
        for i in range(K):
            learnData = []
            testData = []
            for j in range(K):
                if i == j:
                    testData = dataListList[j]
                else:
                    learnData += dataListList[j]

            logistic = LogisticRegulationCrossValidation(learnData,testData,0.1,100,th)
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
        results.append({"th":th,"p":precision,"r":recall})

    f = open("result.txt","w")
    for result in results:
        f.write("%f,%f,%f\n" % (result["th"],result["p"],result["r"]))

    PList = map(lambda n:n["p"],results)
    RList = map(lambda n:n["r"],results)
    plt.plot(RList,PList,"o")
#plt.show()
    plt.savefig("graph.png")

