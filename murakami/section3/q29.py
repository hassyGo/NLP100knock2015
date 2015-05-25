#!/usr/bin/env python
#coding: utf-8

"""
    29. 国旗画像のURLを取得する
    テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import json
import string
import re
import urllib2

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
    
        for n in re.finditer(u'\[\[.*\]\]',value):
            before = n.group()
            after = re.sub(u'[\[\]]','',before)
            value = value.replace(before,after)
        
        for n in re.finditer(u'<ref.*?/>|<ref.*?</ref>|<br.?/>',value):
            value = value.replace(n.group(),"")
        
        dic[field] = value

    ##26-28 ------------------------------------

    filename = dic[u"国旗画像"]
    #print filename
    apiurl = "http://en.wikipedia.org/w/api.php?action=query&titles=Image:" + filename.replace(" ","%20") + "&prop=imageinfo&iiprop=url&format=json"
    #print apiurl
    apijson = []
    r = urllib2.urlopen(apiurl)
    lines = r.readlines()
    for line in lines:
        apijson.append(json.loads(line))

    imageurl = apijson[0]["query"]["pages"]["23473560"]["imageinfo"][0]["url"]
    print imageurl
