#!/usr/bin/env python
#coding: utf-8

"""
    39. Zipfの法則
    単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import q30
import q36


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    countDic = q36.getFrequency(lists)

    freq = sorted(countDic.items(), key=lambda x:x[1], reverse = True)[0:100]
    
    rank = range(len(freq))
    count = [i[1] for i in freq]
    

    plt.xscale('log')
    plt.yscale('log')
    plt.plot(rank,count)
    plt.show()
