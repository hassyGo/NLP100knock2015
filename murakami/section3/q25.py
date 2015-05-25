#!/usr/bin/env python
#coding: utf-8

"""
    25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import json
import string
import re

import q20

if __name__ == "__main__":
    jsonData = q20.readJson("england.json")[0]
    text = jsonData["text"]
    
    dic = {}
    
    basicInfoString = re.search(u'{{基礎情報.*?\n}}',text,re.DOTALL).group()
    for m in re.finditer(u'\|.* = .*',basicInfoString):
        infoString = m.group()
        field = re.search(u'\|.*? =',infoString).group()[1:-2]
        value = re.search(u'= .*',infoString).group()[2:]
        dic[field] = value

    q20.printDict(dic)
