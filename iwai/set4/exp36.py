# !/usr/bin/python
# coding:UTF-8
# 4-(36)

from collections import Counter
import sys
import re
import copy

f = open("neko.txt.mecab", "r")
fw = open("36.txt", "w")
sys.stdout = fw

subset = []
all = []
lst = []

cnt = Counter()
words = {}

for line in f.readlines():
    d = {}
    line = line.strip()
    if line == "EOS":
        all.append(copy.copy(subset))
        del subset[:]
    else:
        line = line.split("\t")
        fir = line[0]
        sec = line[1]
        d['surface'] = line[0]
        sec = sec.split(",")
        d['base'] = sec[6]
        d['pos'] = sec[0]
        d['pos1'] = sec[1]
        subset.append(d)

for i in all:
    for j in i:
        words[j['surface']] = words.get(j['surface'], 0) + 1

d = [(v,k) for k,v in words.items()]

d.sort()
d.reverse()

for key, value in d:
    print key, value


"""
for i in all:
    for j in i:
        cnt[j['surface']] += 1

sorted(cnt)

for i in cnt.items():
    print i
#昇順にはなるんだけど！
#for key in sorted(cnt.items(), key=lambda x:x[1]):
#    print key

#for i in cnt.items():
#    print i
"""
"""
#cntの中身を表示させる
for i in cnt.items():
    print i[0]+":",
    print i[1]
"""
f.close()
fw.close()
