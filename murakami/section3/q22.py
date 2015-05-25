#!/usr/bin/env python
#coding: utf-8

"""
    22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import json
import string
import re

import q20


if __name__ == "__main__":
    jsonData = q20.readJson("england.json")[0]
    text = jsonData["text"]

    for line in text.split("\n"):
        if(re.match('\[\[Category:',line) != None):
            category = line.split("[[Category:")[1].split("]")[0]
            print category