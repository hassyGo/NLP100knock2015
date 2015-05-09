# -*- coding: utf-8 -*-


#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．


import string
import sys
import math
import itertools

if __name__ == "__main__":
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()

    col1 = [line.split()[0] for line in lines]
    
    set1 = sorted(set(col1))

    list = [(x,col1.count(x)) for x in set1]
    list.sort(key=lambda x:(x[1]))

    for x in list:
        print x[0],x[1]

#コマンドでやるなら
# cut -f 1 hightemp.txt > col1.txt
# sort (-k 1,1) col1.txt > sort.txt
# uniq -c sort.txt > sortCount.txt
# sort -k 1,1 sortCount.txt