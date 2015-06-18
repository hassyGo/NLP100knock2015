#!/usr/bin/env python
#coding: utf-8

"""
    37. 頻度上位10語
    出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ
"""

import q30
import q36


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    countDic = q36.getFrequency(lists)

    freq = sorted(countDic.items(), key=lambda x:x[1], reverse = True)[0:10]
    
    X = range(len(freq))
    Y = [i[1] for i in freq]

    plt.bar(X,Y,align="center")
    #plt.xticks(X,[i[0] for i in freq])
    plt.show()
