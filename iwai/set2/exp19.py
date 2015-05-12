# !/usr/bin/python
# coding:UTF-8
# 2-(19)

from collections import Counter
import codecs
import sys

f = codecs.open("col1.txt", "r")

lst =[]

cnt = Counter()
for word in f.readlines():
    word = word.strip()
    cnt[word] += 1
#    print cnt

for i in cnt.items():
    print i[0]+ ":" ,
    print i[1]
#print cnt
"""
for i in cnt.items():
    print i
"""
f.close()
