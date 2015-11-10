#!/usr/bin/env python
#coding: utf-8

"""
    77. 正解率の計測
    76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
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

    logistic.learningCheck(True)