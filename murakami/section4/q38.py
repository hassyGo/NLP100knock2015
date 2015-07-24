#!/usr/bin/env python
#coding: utf-8

"""
    38. ヒストグラム
    単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import q30
import q36


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    countDic = q36.getFrequency(lists)

    freq = sorted(countDic.items(), key=lambda x:x[1], reverse = True)[0:100]
    
    data = [i[1] for i in freq]
  

    plt.hist(data,bins = 10)
    plt.show()
