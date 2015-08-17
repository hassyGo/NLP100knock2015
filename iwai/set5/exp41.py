# !/usr/bin/python
# coding:UTF-8
# 4-(41)のcopy, defとか使って編集したver.

import sys
import re
import exp40_copy as exp40

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

if __name__ == "__main__":
    fw = open("41copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    
    subset = []
    all = []
    chunks = []
    sentence = []
    phrase = {0:[0]}

    for line in document:
        match = exp40.search_sentence(line)

        if line == "EOS":
            all.append(sentence)
            sentence = []
            phrase = {}
        elif match:
            c = Chunk(line)
            sentence.append(c)
        else:
            sentence[-1].morphs.append(exp40.Morph(line))

    for i in all[0]:
        print "dst =", i.dst
        print "srcs =", i.srcs
        for j in i.morphs:
            print j.surface, j.base, j.pos, j.pos1

    fw.close()

