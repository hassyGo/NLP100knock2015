#!/usr/bin/env python
#coding: utf-8

"""
    43. 名詞を含む文節が動詞を含む文節に係るものを抽出
    名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""


from q40 import *
from q41 import *
from q42 import *


if __name__ == "__main__": #ここでも必要な部品はすべて今までのコード（主にq40,q41）で作成済みなので、それを利用する

    sentences = makeSentenceListFromXml("neko.xml") #毎度おなじみ、xmlファイルからchunkのリストのリストを作る

    for s in sentences:
        for c in s:
            if c.dst != -1:
                if c.isIncludePos("名詞") and s[c.dst].isIncludePos("動詞"): #名詞が入っていてかつ、かかり先が動詞がはいっているか調べる。
                    print "%s\t%s" % (c.getText(),s[c.dst].getText()) #条件をみたしたら、表示する。
                    #getText()は、文節の文字列を取得する関数