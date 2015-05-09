# -*- coding: utf-8 -*-

#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．


import string
import sys

if __name__ == "__main__":
    
    N = int(sys.argv[1])
    print N
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()

    for line in lines[-N:]:
        print line.rstrip()

#コマンドでやるなら
# tail -n 10 hightemp.txt