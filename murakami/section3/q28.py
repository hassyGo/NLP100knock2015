#!/usr/bin/env python
#coding: utf-8

"""
    28. MediaWikiマークアップの除去
    27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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
        
        #26----------
        for n in re.finditer(u"''+.*''+",value):
            before = n.group()
            after = re.sub(u"''+","",before)
            value = value.replace(before,after)
        #------------
        #27----------
        for n in re.finditer(u'\[\[.*\]\]',value):
            before = n.group()
            after = re.sub(u'[\[\]]','',before)
            value = value.replace(before,after)
        #------------
        
        for n in re.finditer(u'<ref.*?/>|<ref.*?</ref>|<br.?/>',value):
            value = value.replace(n.group(),"")
        
       
        dic[field] = value

q20.printDict(dic)
