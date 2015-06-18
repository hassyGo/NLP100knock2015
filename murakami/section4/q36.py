#!/usr/bin/env python
#coding: utf-8

"""
    36. 単語の出現頻度
    文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import q30


def getFrequency(lists):
    countDic = {}
    for l in lists:
        for dic in l:
            surface = dic["surface"]
            if surface in countDic:
                countDic[surface] += 1
            else:
                countDic[surface] = 1
    return countDic


if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")

    countDic = getFrequency(lists)

    for k, v in sorted(countDic.items(), key=lambda x:x[1], reverse=True):
        if v>=100:
            print k, v
