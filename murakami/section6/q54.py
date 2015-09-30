#!/usr/bin/env python
#coding: utf-8

"""
    54. 品詞タグ付け
    Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""


from q53 import *


if __name__ == "__main__":
    root = readXml("nlp.txt.xml") #xmlから木構造を作る
    
    for token in root.iter("token"): #<token> ... </token>のノードを再帰的に探索してくれる
        word = token.find("word").text #<token>内の<word>タグに相当するノードを取得
        lemma = token.find("lemma").text
        pos = token.find("POS").text

        print "{}\t{}\t{}".format(word,lemma,pos)