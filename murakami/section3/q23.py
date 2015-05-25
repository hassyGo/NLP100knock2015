#!/usr/bin/env python
#coding: utf-8

"""
    23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import json
import string
import re

import q20


if __name__ == "__main__":
    jsonData = q20.readJson("england.json")[0]
    text = jsonData["text"]

    for line in text.split("\n"):
        if(re.match(r'=.*?=',line) != None):
            level = (len(line.split("=")) - 1) / 2 - 1
            print line.split("=")[level+1],level