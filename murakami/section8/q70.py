#!/usr/bin/env python
#coding: utf-8

"""
    70. データの入手・整形
    文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
    
    rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
    rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
    上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
    sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""

import random


if __name__ == "__main__":
    fpos = open("./rt-polaritydata/rt-polaritydata/rt-polarity.pos")
    poslines = ["+1 " + line.rstrip() for line in fpos.readlines()]
    
    fneg = open("./rt-polaritydata/rt-polaritydata/rt-polarity.neg")
    neglines = ["-1 " + line.rstrip() for line in fneg.readlines()]
    
    print "pos:%d neg:%d" % (len(poslines),len(neglines))

    poslines.extend(neglines)
    random.shuffle(poslines)
    
    fout = open("sentiment.txt","w")
    fout.write("\n".join(poslines))