#!/usr/bin/env python
#coding: utf-8

"""
    35. 名詞の連接
    名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import q30


if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    #longest = []
    nounSeq = []
    for l in lists:
        tmplist = []
        for dic in l:
            if dic["pos"] == "名詞":
                tmplist.append(dic["surface"])
            else:
                #if len(longest) <= len(tmplist):
                #    longest = list(tmplist)
                if len(tmplist) >= 2:
                    nounSeq.append(list(tmplist))
                tmplist = []

#for l in longest:
#    print l

    for seq in nounSeq:
        print seq