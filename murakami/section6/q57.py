#!/usr/bin/env python
#coding: utf-8

"""
    57. 係り受け解析
    Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""


from q53 import *

import pydot



if __name__ == "__main__":
    root = readXml("nlp_sample.txt.xml") #xmlから木構造を作る

    edges = []

    for sentences in root.iter("sentences"):
        for sentence in sentences.iter("sentence"):
            sentenceId = sentence.get("id")
            for dependency in sentence.iter("dependencies"):
                if dependency.get("type") == "collapsed-dependencies":
                    for dep in dependency.iter("dep"):
                        type = dep.get("type")
                        gov = "%s(%s,%s)" % (dep.find("governor").text,sentenceId,dep.find("governor").get("idx"))
                        dependent = "%s(%s,%s)" % (dep.find("dependent").text,sentenceId,dep.find("dependent").get("idx"))

                        edges.append((gov,dependent))
#graph = pydot.Doc(graph_type='')
#graph.add_edge(edge)
#graph.write_png("aaa.png")

#StanfordCoreNLPではtodotformat()として、出力をdot言語にできる

    g = pydot.graph_from_edges(edges,directed=True)
    g.write_jpeg("dot.jpg",prog = "dot")