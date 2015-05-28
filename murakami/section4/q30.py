#!/usr/bin/env python
#coding: utf-8

"""
    30. 形態素解析結果の読み込み
    形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def printDict(dic):
    print "{"
    for k,v in dic.items():
        print "\t",k,":",v
    print "}"

def readMecab(filename):
    
    lists = []
    tmplist = []
    
    print filename
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        if(line.find("EOS") != -1):
            lists.append(tmplist)
            tmplist = []
        else:
            surface = line.split("\t")[0]
            attributes = line.split("\t")[1].split(",")
            dic = {"surface":surface,"base":attributes[6],"pos":attributes[0],"pos1":attributes[1]}
            tmplist.append(dic)

    return lists
            



if __name__ == "__main__":
    lists = readMecab("neko.txt.mecab")
    print len(lists)
    for l in lists:
       for dic in l:
           printDict(dic)
