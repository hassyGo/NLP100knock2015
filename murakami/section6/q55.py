#!/usr/bin/env python
#coding: utf-8

"""
    55. 固有表現抽出
    入力文中の人名をすべて抜き出せ．
"""


from q53 import *


if __name__ == "__main__":
    root = readXml("nlp.txt.xml") #xmlから木構造を作る
    
    #tree = ET.parse(file)
    #for token in tree.findall(".//token")　でオッケー itertoolいらない
    
    for token in root.iter("token"):#<token> ... </token>のノードを再帰的に探索してくれる
        word = token.find("word").text
        ner = token.find("NER").text

        if ner == "PERSON":
            print word