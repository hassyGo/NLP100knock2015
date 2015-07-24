# !/usr/bin/python
# coding:UTF-8
# 4-(38)

import numpy as np
import matplotlib.pyplot as plt
#import sys
import re
import copy

f = open("neko.txt.mecab", "r")
#data = np.loadtxt("36.txt")

subset = []
all = []
lst = []
x = []
y = []
z = []
cnt = 1
#cnt = Counter()
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
    x.append(key)
    y.append(value)

plt.hist(x, 100)

plt.show()
#plt.savefig('foo.png')

f.close()
