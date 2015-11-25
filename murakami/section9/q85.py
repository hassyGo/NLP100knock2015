#!/usr/bin/env python
#coding: utf-8

"""
    85. 主成分分析による次元圧縮
    84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
"""

from q84 import *


if __name__ == "__main__":
    X = {}
    f = open("XMatrix.txt")
    line = f.readline()
    while line:
        if line == "":continue
        elements 
        line = f.readline()
