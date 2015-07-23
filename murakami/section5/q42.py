#!/usr/bin/env python
#coding: utf-8

"""
    42. 係り元と係り先の文節の表示
    係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""


from q40 import *
from q41 import *
import xml.etree.ElementTree as ET
import itertools
import re




if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")

    for s in sentences:
        for c in s:
            if(c.dst != -1):
                print "%s\t%s" % (c.getText(),s[c.dst].getText())