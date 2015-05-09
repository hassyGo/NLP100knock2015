# -*- coding: utf-8 -*-

#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．


import string

if __name__ == "__main__":

    f = open('hightemp.txt')
    lines = f.readlines()
    f.close()
    
    for i in range(2):
        f = open("col%d.txt" % (i+1),"w")
        for line in lines:
            f.write(line.split()[i] + "\n")
        f.close()

#コマンドでやるなら
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt

#http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230738/