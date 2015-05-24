# !/usr/bin/python
# coding:UTF-8
# 3-(21)

import sys
import re

f = open("write.txt", "r")
fw = open("21.txt", "w")
sys.stdout = fw

lst = []

for line in f.readlines():
    s1 = re.search("^\[\[カテゴリ:[ぁ-ん一-龥]+|^\[\[Category:[ぁ-ん一-龥]+", line)
#    s2 = re.search("^\[\[カテゴリ:([一-龥])|^\[\[Category:([一-龥])", line)
    if s1:
        print line,

f.close()
fw.close()
