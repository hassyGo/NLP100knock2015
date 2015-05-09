# -*- coding: utf-8 -*-

#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．



import string
import sys
import math
import itertools

if __name__ == "__main__":
    
    f = open("hightemp.txt")
    lines = f.readlines()
    f.close()

    lists = [line.split() for line in lines]
    
    lists.sort(key=lambda x:(x[2]) ,reverse=True)

    for list in lists:
        print "\t".join(list)

#コマンドでやるなら
# sort -r -k 3,1 hightemp.txt 