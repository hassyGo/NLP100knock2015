#!/usr/bin/env python
#coding: utf-8

"""
    51. 単語の切り出し
    空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""

from q50 import *



if __name__ == "__main__":
    f = open("./nlp.txt","r")
    lines = f.readlines()
    for line in lines:
        sentences = splitSentences(line.rstrip())
        for sentence in sentences:
            words = sentence.split(" ")
            for word in words:
                print word
            print ""