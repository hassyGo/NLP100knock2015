# !/usr/bin/python
# coding:UTF-8
# 4-(32)

import sys
import re
import copy

f = open("neko.txt.mecab", "r")
fw = open("32.txt", "w")
sys.stdout = fw

all = []
subset = []

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
        for key, value in j.items():
            if value == "動詞":
                print j['base']


f.close()
fw.close()
