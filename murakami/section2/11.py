# -*- coding: utf-8 -*-

#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．


import string

if __name__ == "__main__":

    f = open('hightemp.txt')
    lines = f.readlines()
    f.close()
    
    lines = [line.translate(string.maketrans('\t',' ')) for line in lines]
    for line in lines:
        print line.rstrip()



#コマンドでやるなら
# sed $'s/\t/ /g' hightemp.txt

# cat hightemp.txt | tr '\t' ' '

# expand -t 1 hightemp.txt