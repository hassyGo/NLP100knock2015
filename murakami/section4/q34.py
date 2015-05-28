#!/usr/bin/env python
#coding: utf-8

"""
    34. 「AのB」
    2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import q30


if __name__ == "__main__":
    lists = q30.readMecab("neko.txt.mecab")
    print len(lists)
    for l in lists:
        if(len(l)>=3):
            for dic1,dic2,dic3 in zip(l,l[1:],l[2:]):
                if(dic1["pos"] == "名詞" and dic3["pos"] == "名詞" and dic2["surface"] == "の"):
                    print dic1["surface"] + dic2["surface"] + dic3["surface"]
