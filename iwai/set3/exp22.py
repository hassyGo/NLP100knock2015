# !/usr/bin/python
# coding:UTF-8
# 3-(22)

import sys
import re

f = open("write.txt", "r")
fw = open("22.txt", "w")
sys.stdout = fw

lst = []

for line in f.readlines():
    s1 = re.search("^\[\[カテゴリ:([ぁ-ん一-龥]+)", line)
    s2 = re.search("^\[\[Category:([ぁ-ん一-龥]+)", line)
#    s1 = re.search("\[カテゴリ:([ぁ-ん]+)|\[Category:([ぁ-ん]+)", line)
#    s2 = re.search("\[カテゴリ:([一-龥])|\[Category:([一-龥])", line)
    if s1:
        print line,
        print s1.group(1)

    if s2:
        print line,
        print s2.group(1)

f.close()
fw.close()
