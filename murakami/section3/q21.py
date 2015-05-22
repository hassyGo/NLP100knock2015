#!/usr/bin/env python
#coding: utf-8

"""
    21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import json
import string
import re

import q20


if __name__ == "__main__":
    jsonData = q20.readJson("england.json")[0]
    text = jsonData["text"]

    for line in text.split("\n"):
        if(re.match(r'\[\[Category',line) != None):
            print line