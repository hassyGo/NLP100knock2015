# -*- coding: utf-8 -*-

#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．


import string
import sys

if __name__ == "__main__":
    
    N = int(sys.argv[1])
    print N
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()

    for line in lines[:N]:
        print line.rstrip()

#コマンドでやるなら
# head -n 10 hightemp.txt