#!/usr/bin/env python
#coding: utf-8

"""
    50. 文区切り
    (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""


import re

def splitSentences(line):#一行分の文章を文単位に分割する
    sentences = []
    string = line
    while True:
        a = re.search('[.;:?!]\s[A-Z]',string)
        if a == None:
            break
        else:
            sentences.append(string[0:a.start()+1])
            string = string[a.end()-1:]

    sentences.append(string)
    return sentences


if __name__ == "__main__":
    f = open("./nlp.txt","r")
    lines = f.readlines()
    for line in lines:
        sentences = splitSentences(line.rstrip())
        for sentence in sentences:
            print sentence
