#!/usr/bin/env python
#coding: utf-8

"""
    75. 素性の重み
    73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

from q71 import *
from q72 import *
from q73 import *
import numpy as np
import math



if __name__ == "__main__":

    wordlist = makeWordlist("sentiment.txt",getStopWordList())
    dictionary = {"wordlist":wordlist}
    dataList = makeData("sentiment.txt",dictionary)

    logistic = LogisticRegulation(dataList,0.1,100)
    logistic.readWeightVec("weight.txt")

    dic = [(i,logistic.weightVec[i]) for i in range(len(logistic.weightVec))]
    sort_dic = sorted(dic, key=lambda x: x[1])
    top10index = map(lambda n:n[0],sort_dic[-10:])
    worst10index = map(lambda n:n[0],sort_dic[0:10])
    top10feature = [wordlist[m] for m in top10index];
    worst10feature = [wordlist[m] for m in worst10index];
    print "top10",top10feature
    print "worst10",worst10feature