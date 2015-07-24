# !/usr/bin/python
# coding:UTF-8
# 4-(35)

import sys
import re
import copy

f = open("neko.txt.mecab", "r")
fw = open("35new.txt", "w")
sys.stdout = fw

subset = []
all = []
str = []

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
        if j['pos'] == "名詞":
            str.append(j['surface'])
        else:
            if len(str) > 1:
                print "".join(str)
#            for i in str:
#                print str[0]
#            for item in str:
#                print item
            del str[:]

f.close()
fw.close()
