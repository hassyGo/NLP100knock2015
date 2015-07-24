# !/usr/bin/python
# coding:UTF-8
# 4-(45)

import sys
import re
import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("45.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
frame = []
VP = []
particle = []
phrase = {0:[0]}
pairs = []
cnt = 1
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
        all.append(subset)
        subset = []
        phrase = {}

    elif match:
        c = Chunk(line)
        subset.append(c)

    else:
        subset[-1].morphs.append(Morph(line))

for i in all:
#    print i
    for j in i:
        if j.srcs == 'none':
            continue
        else:
            VP = []
            for k in j.morphs:
                if k.pos == '動詞':
                    VP.append(k.base)
                    break
#len(VP)いれて動詞の有無をチェック

            for k in j.srcs:
#                print  i[int(k)].morphs[-1]
                for l in i[int(k)].morphs[::-1]:
                    if l.pos == '助詞':
#                        print l.surface
#                        break
#                print '\n'.strip()
#                i[int(k)].morphs
#                    if l.pos == '助詞':
                        particle.append(l.surface)
                        break
            VP.append(particle)
            particle = []
            frame.append(VP)

for i in frame:
    if len(i) == 2:
        if len(i[1]) == 0:
            continue
        else:
            i[1].sort()
            print i[0], '\t', " ".join(i[1])

f.close()
fw.close()

