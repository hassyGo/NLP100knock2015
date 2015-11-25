#!/usr/bin/env python
#coding: utf-8

"""
    83. 単語／文脈の頻度の計測
    82の出力を利用し，以下の出現分布，および定数を求めよ．
    
    f(t,c): 単語tと文脈語cの共起回数
    f(t,∗): 単語tの出現回数
    f(∗,c): 文脈語cの出現回数
    N: 単語と文脈語のペアの総出現回数
"""


if __name__ == "__main__":
    f = open("context_words.txt")
    
    countTC = {}
    countT = {}
    countC = {}
    countN = 0
    
    line = f.readline()
    while line:
        if line == "": continue
        t = line.rstrip().split("\t")[0]
        c = line.rstrip().split("\t")[1]
        
        if t in countTC:
            if c in countTC[t]:
                countTC[t][c] += 1
            else:
                countTC[t][c] = 1
        else:
            countTC[t] = {c:1}
        
        if t in countT:
            countT[t] += 1
        else:
            countT[t] = 1

        if c in countC:
            countC[c] += 1
        else:
            countC[c] = 1

        countN += 1
        
        line = f.readline()

    f.close()

    fo = open("countTC.txt","w")
    for tk,tv in countTC.items():
        for ck,cv in tv.items():
            fo.write("%s\t%s\t%d\n" % (tk,ck,cv))
    fo.close()

    fo = open("countT.txt","w")
    for k,v in countT.items():
        fo.write("%s\t%d\n" % (k,v))
    fo.close()

    fo = open("countC.txt","w")
    for k,v in countC.items():
        fo.write("%s\t%d\n" % (k,v))
    fo.close()

    fo = open("countN.txt","w")
    fo.write("%d\n" % countN)
    fo.close()
