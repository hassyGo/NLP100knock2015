#!/usr/bin/env python
#coding: utf-8

"""
    33. サ変名詞
    サ変接続の名詞をすべて抽出せよ．
"""

import q30


if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    print len(lists)
    for l in lists:
        for dic in l:
            if(dic["pos"] == "名詞" and dic["pos1"] == "サ変接続"):
                print dic["base"]
