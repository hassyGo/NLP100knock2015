# !/usr/bin/python
# coding:UTF-8
# 4-(40)

import sys
import re
import copy

f = open("neko.txt.cabocha", "r")
fw = open("40.txt", "w")
sys.stdout = fw

subset = []
all = []

class Morph:
    def __init__(self, line):
        line = line.split("\t")
        self.surface = line[0]
        word = line[1].split(",")
        self.base = word[6]
        #self.base = word[-3]でも同じことができる(後ろから参照)
        self.pos = word[0]
        self.pos1 = word[1]

for line in f.readlines():
    line = line.strip()
    r = re.compile("\*")
    match = r.match(line)
#    match = re.match("^\*", line)
    if line == "EOS":
        """
        for i in subset:
            print i.surface, "\t", i.base, i.pos, i.pos1
#            print i.base
        """
        all.append(subset)
        subset = []
    elif match:
        continue
    else:
        subset.append(Morph(line))

for i in all[5]:
    print i.surface, i.base, i.pos, i.pos1
#all print
"""
for i in all:
    for item in i:
        print item.surface, item.base, item.pos, item.pos1
    print "\n".strip()
"""
f.close()
fw.close()

