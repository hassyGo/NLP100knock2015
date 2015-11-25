#!/usr/bin/env python
#coding: utf-8

"""
    htmlから複数語の国名を抽出する
    http://www6.kaiho.mlit.go.jp/isewan/image/flags/_flags.htm
"""

import re

if __name__ == "__main__":
    fo = open("countries.txt","w")
    
    f = open("国旗と国名一覧(５０音順).html")
    lines = f.readlines()
    for line in lines:
        match = re.findall("(<td>.*?</td>)",line.strip())
        if match:
            countryName = match[1][4:-5]
            if len(countryName.split()) >= 2:
                fo.write(countryName+"\n")