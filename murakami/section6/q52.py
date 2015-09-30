#!/usr/bin/env python
#coding: utf-8

"""
    52. ステミング
    51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

from q50 import *
from stemming.porter2 import stem

if __name__ == "__main__":
    f = open("./nlp.txt","r")
    lines = f.readlines()
    for line in lines:
        sentences = splitSentences(line.rstrip())
        for sentence in sentences:
            words = sentence.split(" ")
            for word in words:
                print "%s\t%s" % (word,stem(word))
            print ""