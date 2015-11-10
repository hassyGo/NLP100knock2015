#!/usr/bin/env python
#coding: utf-8

"""
    76. ラベル付け
    学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
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