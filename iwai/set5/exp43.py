# !/usr/bin/python
# coding:UTF-8
# 4-(43)

import sys
import re
import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("43.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
pairs = []

r = re.compile("\*")
#k = 0

class Morph:
    def __init__(self, line):
        line = line.split("\t")
        self.surface = line[0]
        word = line[1].split(",")
        self.base = word[6]
        self.pos = word[0]
        self.pos1 = word[1]

class Chunk:
    def __init__(self, line):
        line = re.sub(r"D", "", line)
        line = line.split()
        self.dst = line[2]
        self.morphs = []
        if line[2] not in phrase:
            phrase[line[2]] = [line[1]]
        else:
            phrase[line[2]].append(line[1])
        if line[1] in phrase:
            self.srcs = phrase[line[1]]
        else:
            self.srcs = "none"        

for line in f.readlines():
    line = line.strip()
    match = r.match(line)
    if line == "EOS":
        all.append(sentence)
        sentence = []
        phrase = {}

    elif match:
        c = Chunk(line)
        sentence.append(c)

    else:
        sentence[-1].morphs.append(Morph(line))

for i in all:
    for j in i:
        if j.srcs == 'none':
            continue
        else:
            for k in j.srcs:
                a = i[int(k)].morphs
                b = j.morphs
                pair = a,b
                pairs.append(pair)

for i in pairs:
    k1 = 0
    k2 = 0
#    if '名詞' in list
#    j.pos for j in i[0]

    for j in i[0]:
        if j.pos == '記号':
            continue
        else:
            if j.pos == '名詞':
                k1 = 1
                break
    for j in i[1]:
        if j.pos == '記号':
            continue
        else:
            if j.pos == '動詞':
                k2 = 1
                break
    if k1 == 1 and k2 == 1:
        for j in i[0]:
            if j.pos == '記号':
                continue
            else:
                sys.stdout.write(j.surface)
        print '\t',
        for j in i[1]:
            if j.pos == '記号':
                continue
            else:
                sys.stdout.write(j.surface)
        print '\n'.strip()
            
f.close()
fw.close()

