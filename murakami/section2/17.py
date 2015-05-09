# -*- coding: utf-8 -*-

#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．



import sys
import math
import itertools

#optparse　が便利：コマンドライン入力でオプションをつけれる

if __name__ == "__main__":
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()

    set1 = sorted(set([line.split()[0] for line in lines]))
    
    for x in set1:
        print x

#コマンドでやるなら
# sort (-k 1,1) col1.txt > sort.txt
# uniq sort.txt