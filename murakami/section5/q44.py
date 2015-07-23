#!/usr/bin/env python
#coding: utf-8

"""
    44. 係り受け木の可視化
    与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""


from q40 import *
from q41 import *
from q42 import *

import pydot



def showGraph(chunkList):
    edges = []
    for c in chunkList:
        if c.dst != -1:
            edges.append((c.getText().encode('utf-8'),chunkList[c.dst].getText().encode('utf-8')))

    g = pydot.graph_from_edges(edges,directed = True)
    g.write_jpeg('dot.jpg', prog='dot')


if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    showGraph(sentences[5])