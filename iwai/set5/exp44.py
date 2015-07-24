# !/usr/bin/python
# coding:UTF-8
# 4-(44)

import sys
import re
import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("44.dot", "w")
sys.stdout = fw

test = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
pairs = []

r = re.compile("\*")

argv = sys.argv
argc = len(argv)

n = int(sys.argv[1])

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
    test.append(pairs)
    pairs = []

print 'digraph sample{'
print '', 'graph [rankdir = LR];'
for i in test[n]:
    for j in i[0]:
        sys.stdout.write(j.surface)
    print '->',
    for j in i[1]:
        sys.stdout.write(j.surface)
    print '\n'.strip()
print '}'

f.close()
fw.close()

