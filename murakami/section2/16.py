# -*- coding: utf-8 -*-

#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

#http://stackoverflow.com/questions/2233204/how-does-zipitersn-work-in-python

import string
import sys
import math
import itertools

if __name__ == "__main__":
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()
    
    N = int(sys.argv[1])
    size = int(math.ceil(len(lines)*1.0/N))

    for tuple in itertools.izip_longest(*[iter(lines)]*size):
        for line in tuple:
            print line.rstrip()
        print

#コマンドでやるなら
# split -l 24/N hightemp.txt