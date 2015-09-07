#!/usr/bin/env python
#coding: utf-8

"""
    53. Tokenization
    Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""


import xml.etree.ElementTree as ET #xmlファイルから自動的に木構造を生成するライブラリ
import itertools #その木構造のイテレーションを制御するためのライブラリ


def readXml(filename): #filenameを文字列で渡してあげると、自動的にxmlデータから木構造を作ってくれる。最終的にもどってくるのはrootノードの情報。これをもとに木を巡回する。
    with open(filename) as f:
        it = itertools.chain(f)#もしルートタグがない場合はつける
        root = ET.fromstringlist(it)
    return root

if __name__ == "__main__":
    root = readXml("nlp.txt.xml") #xmlから木構造を作る
    
    for word in root.iter("word"):#<word> ... </word>のノードを再帰的に探索してくれる
        print word.text
