# !/usr/bin/python
# coding:UTF-8
# 4-(37)

import numpy as np
import matplotlib.pyplot as plt
#import sys
import re
import copy

f = open("neko.txt.mecab", "r")
#fw = open("37.txt", "w")
#sys.stdout = fw

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

for key, value in d[:10]:
    x.append(cnt)
    cnt += 1
    y.append(key)
    z.append(value)
#    print key, value
plt.bar(x,y, align="center")
plt.xticks(x, [z[0].decode('utf-8'), z[1].decode('utf-8'), z[2].decode('utf-8'), z[3].decode('utf-8'), z[4].decode('utf-8'), z[5].decode('utf-8'), z[6].decode('utf-8'), z[7].decode('utf-8'), z[8].decode('utf-8'), z[9].decode('utf-8')])

plt.show()
#plt.savefig('foo.png')

f.close()
#fw.close()
