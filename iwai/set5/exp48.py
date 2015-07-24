# !/usr/bin/python
# coding:UTF-8
# 4-(48)

import sys
import re
#import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("48.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
pair = []
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
##    print i
    flag1 = 0
    flag2 = 0
    for j in i: 
        if j.dst == '-1':
            continue
        else:
            for k in j.morphs:
                if k.pos == '名詞':
                    flag1 = 1
                if flag1 == 1:
                    pair.append(k.surface)
#                    flag2 = 1
            pair.append(" -> ")
            if flag1 == 1:
                n = int(j.dst)
                while n != -1:
                    for morph in i[n].morphs:
                        if morph.pos == '記号':
                            continue
                        else:
                            pair.append(morph.surface)
                    pair.append(" -> ")
                    n = int(i[n].dst)
#                for k in 
            flag1 = 0
#            flag2 = 0
            pairs.append(pair)
            pair = []

#print ->

for i in pairs:
#    print i
    if len(i) == 1:
        continue
    else:
        i.pop()            
        print "".join(i)


f.close()
fw.close()


