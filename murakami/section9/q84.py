#!/usr/bin/env python
#coding: utf-8

"""
    84. 単語文脈行列の作成
    83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
    
    f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
    f(t,c)<10ならば，Xtc=0
    ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
"""

import math
import sys

class Counter:
    def __init__(self):
        print "loading countTC.txt"
        self.tcDic = {}
        f = open("countTC.txt")
        line = f.readline()
        i = 0
        while line:
            if line == "":continue
            self.tcDic[",".join(line.split("\t")[0:2])] = int(line.split("\t")[2])
            line = f.readline()
            i+=1
            if i % 1000000 == 0:
                print i*1.0 / 21328325 * 100
        f.close()

        print "loading countT.txt"
        self.tDic = {}
        f = open("countT.txt")
        line = f.readline()
        while line:
            if line == "":continue
            self.tDic[line.split("\t")[0]] = int(line.split("\t")[1])
            line = f.readline()
        f.close()

        print "loading countC.txt"
        self.cDic = {}
        f = open("countC.txt")
        line = f.readline()
        while line:
            if line == "":continue
            self.cDic[line.split("\t")[0]] = int(line.split("\t")[1])
            line = f.readline()
        f.close()

        f = open("countN.txt")
        self.N = int(f.readline().rstrip())
        f.close()

    def f_tc(self,t,c):
        key = "%s,%s" % (t,c)
        if key in self.tcDic:
            return self.tcDic[key]
        return 0

    def f_t(self,t):
        return self.tDic[t]

    def f_c(self,c):
        return self.cDic[c]


def word_list():
    list = []
    f = open("countT.txt")
    line = f.readline()
    while line:
        if line == "": continue
        list.append(line.split("\t")[0])
        line = f.readline()
    return list


def x_tc(t,c,counter):
    if counter.f_tc(t,c) < 10:
        return 0
    return max(0,math.log( counter.N * counter.f_tc(t,c)*1.0 / (counter.f_t(t) * counter.f_c(c) * 1.0) ))


def split_list(list, div ,i):
    l = len(list)
    size = l / div
    if div == i:
        return list[size*(i-1):]
    return list[size*(i-1):size*i]



def makeXMatirx(wordList,div,begin):
    counter = Counter()
    X = {}
    i = 0
    partList = split_list(wordList,div,begin)
    for t in partList:
        i += 1
        print "%d/%d t=%s" % (i,len(partList),t)
        X[t] = {}
        for c in wordList:
            Xtc = x_tc(t,c,counter)
            if(Xtc != 0):
                X[t][c] = Xtc
    return X

if __name__ == "__main__":
    params = sys.argv
    div = 1
    begin = 1
    if len(params) >= 3:
        div = int(params[2])
        begin = int(params[1])
    
    
    X = makeXMatirx(word_list(),div,begin)

    fo = open("XMatrix%d-%d.txt" % (begin,div),"w")
    for t,d in X.items():
        fo.write("%s\t%s\n" % (t,"\t".join(["%s:%f" % (c,v) for c,v in d.items()])));
    fo.close()



