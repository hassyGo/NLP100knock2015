#!/usr/bin/env python
#coding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
import pprint


def readJson(filename):
    jsonData = []
    
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        jsonData.append(json.loads(line))

    f.close()
    return jsonData

def printJson(jsonData):
    print json.dumps(jsonData ,sort_keys = True , ensure_ascii = False , indent = 4)

def printDict(dic):
    for k,v in dic.items():
        print k,":",v

if __name__ == "__main__":
    jsonData = readJson("jawiki-country.json")
    
    for dic in jsonData:
        if(dic["title"] == u"イギリス"):
            printJson(dic)
            f = open("england.json","w");
            f.write(json.JSONEncoder().encode(dic))
            f.close()
