#!/usr/bin/env python
#coding: utf-8

"""
    82. 文脈の抽出
    81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
    
    ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
    単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""

import random

if __name__ == "__main__":
    fo = open("context_words.txt","w")
    f = open("enwiki_country_connected.txt")
    line = f.readline()

    while line:
        words = line.rstrip().split()
        for i in range(len(words)):
            t = words[i]
            d = random.randint(1,5)
            for j in range(i-d,i+d+1):
                if j < 0 or j >= len(words) or j == i :continue
                c = words[j]
                fo.write("%s\t%s\n" % (t,c))
        line = f.readline()