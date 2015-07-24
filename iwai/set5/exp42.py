# !/usr/bin/python
# coding:UTF-8
# 4-(42)

import sys
import re
import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("42.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
pairs = []

r = re.compile("\*")


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
#            if len(j.srcs) == 1:
            for k in j.srcs:
                a = i[int(k)].morphs
                b = j.morphs
                pair = a,b
                pairs.append(pair)
#            else:
#                for k in j.srcs:
#                    a = i[int(k)]

for i in pairs:
    for j in i[0]:
        if j.pos == '記号':
            continue
        else:
            sys.stdout.write(j.surface)
#    print 'tab',
    print '\t',
    for j in i[1]:
        if j.pos == '記号':
            continue
        else:
            sys.stdout.write(j.surface)
    print '\n'.strip()


#orig ver.
"""
for i in all:
    for j in i:
        if j.srcs == "none":
            continue
        else:
            if len(j.srcs) == 1:
                for k in j.srcs:
                    for l in  i[int(k)].morphs:
                        print l.surface,
                    print '\t',
                    for k in j.morphs:
                        if k.pos == '記号':
                            continue
                        else:
                            print k.surface,
                print '\n'
            else:
                for k in j.srcs:
                    for l in i[int(k)].morphs:
                        print l.surface,
                    print '\t', 
                    for k in j.morphs:
                        if k.pos == '記号':
                            continue
                        else:
                            print k.surface,
                    print '\n'
"""

f.close()
fw.close()

