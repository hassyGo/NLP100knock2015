# !/usr/bin/python
# coding:UTF-8
# 6-(50):文区切り
#(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ

import re
import sys

def read(filename):
    lst = []
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip()
        lst.append(line)

    f.close()
    
    return lst

def main():
    fw = open('50.txt', 'w')
    sys.stdout = fw

    document = read('nlp.txt')

    for line in document:
        search = re.search('(\.|\!|\?|\:|\;)\s([A-Z])', line)
        if search:
            print re.sub('(\.|\!|\?|\:|\;)\s[A-Z]', search.group(1)+'\n'+search.group(2), line)

    fw.close()
    
if __name__ == "__main__":
    main()
    
