#!/usr/bin/env python
#coding: utf-8

"""
    42. 係り元と係り先の文節の表示
    係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""


from q40 import *
from q41 import * #こうしておくことで、morphやchunkにまつわるクラスやその関数などをすべて使用できる。
import xml.etree.ElementTree as ET
import itertools
import re




if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml") #q41の関数を読んで、chunkのリストのリストの構造をもつsentencesを取得

    for s in sentences: #sはchunkのリスト
        for c in s: #cはchunkインスタンス
            if(c.dst != -1): #あとはforで順番にイテレーションを回し、かかり先が-1(ない)場合以外を表示し続ける。
                print "%s\t%s" % (c.getText(),s[c.dst].getText())