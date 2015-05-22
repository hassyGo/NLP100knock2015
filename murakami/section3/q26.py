#!/usr/bin/env python
#coding: utf-8

"""
    26. 強調マークアップの除去
    25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
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
            
        for n in re.finditer(u"''+.*''+",value):
            before = n.group()
            after = re.sub(u"''+","",before)
            value = value.replace(before,after)
        
       
        dic[field] = value

    q20.printDict(dic)
