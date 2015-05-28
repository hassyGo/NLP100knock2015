#!/usr/bin/env python
#coding: utf-8

"""
    31. 動詞
    動詞の表層形をすべて抽出せよ．
"""

import q30


if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    print len(lists)
    for l in lists:
        for dic in l:
            if(dic["pos"] == "動詞"):
                print dic["surface"]
