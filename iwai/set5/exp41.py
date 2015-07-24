# !/usr/bin/python
# coding:UTF-8
# 4-(41)

import sys
import re
#import copy

f = open("ichi.txt", "r")
fw = open("41.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
#phrase = {0:[0]
r = re.compile("\*")


class Morph:
    def __init__(self, line):
        line = line.split("\t")
        self.surface = line[0]
        word = line[1].split(",")
        self.base = word[6]
        self.pos = word[0]
        self.pos1 = word[1]

#classに書くべきもの->何回も使いまわすこと,classが持っているものだけで処理できること
#関数を定義してみる

class Chunk:
    def __init__(self, line):
        line = re.sub(r"D", "", line)
        line = line.split()
        self.dst = line[2]
        self.morphs = []
#        print 'case', line[1]
        if line[2] not in phrase:
            phrase[line[2]] = [line[1]]
        else:
#            print line[1], "append to", line[2]
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
#        all.append(chunk)
        sentence = []
#        chunk = []
        phrase = {}

    elif match:
        c = Chunk(line)
        sentence.append(c)

    else:
        sentence[-1].morphs.append(Morph(line))

for i in all[0]:
    print "dst =", i.dst
    print "srcs =", i.srcs
    for j in i.morphs:
        print j.surface, j.base, j.pos, j.pos1

#print all text:
"""
for i in all:
    for j in i:
        print j.dst, j.srcs
        for k in j.morphs:
            print k.surface, k.base, k.pos, k.pos1
"""
f.close()
fw.close()

