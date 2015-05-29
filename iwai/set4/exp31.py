# !/usr/bin/python
# coding:UTF-8
# 4-(31)

import sys
import re
#import copy

f = open("neko.txt.mecab", "r")
fw = open("31.txt", "w")
sys.stdout = fw

all = []
subset = []

for line in f.readlines():
    d = {}
    line = line.strip()
    if line == "EOS":
#        all.append(copy.copy(subset))
#        all.append(subset.copy())
        all.append(list(subset))
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
#        for key, value in j.items():
#            if value == "動詞":
        if j["pos"] == "動詞":
            print j['surface']


f.close()
fw.close()
