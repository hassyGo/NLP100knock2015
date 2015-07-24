# !/usr/bin/python
# coding:UTF-8
# 4-(47)

import sys
import re
import copy
#from __future__ import print_function

f = open("neko.txt.cabocha", "r")
fw = open("47.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
frame = []
VP = []
particle = []
phrase = {0:[0]}
word = []
noun = []
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
    flag = 0
    p1 = 0
    p2 = 0
    for j in i:
        if j.srcs == 'none':
            continue
        else:
            VP = []
            for k in j.morphs:
                if k.pos == '動詞':
                    VP.append(k.base)
                    break
            for k in j.srcs:
                for l in i[int(k)].morphs[::-1]:
                    if l.pos == '助詞':
                        particle.append(l.surface)
                        flag = 1
                        break
                if flag == 1:
                    for m in i[int(k)].morphs:
                        if m.pos == '記号':
                            continue
                        elif m.pos1 == 'サ変接続':
                            p1 = 1
                        else:
#                            print m.surface
#                            if m.pos == '助詞' and m.surface == 'を' or m.pos1 == 'サ変接続':
#                                break
                            word.append(m.surface)
#                            p2 = 0
                        if p1 == 1:
#                            print k
                            for n in i[int(k)].morphs:
#                                print n.surface
                                noun.append(n.surface)
                            if len(particle) == 0:
                                continue
                            else:
                                particle.pop()
                            p1 = 0
#                            for item in word:
#                                print item
#                            word.pop()
                word.append(" ")
                flag = 0
            VP.append(particle)
            if 'を' in noun:        
                VP.append(noun)
            for item1 in noun:
#                print '比較するitem1:',item1
                for item2 in word:
#                    print 'item2:', item2
                    if item1 == item2:
                        word.remove(item2)
#            for item in word:
#                print item
            VP.append(word)
            particle = []
            word = []
            noun = []
            frame.append(VP)

#「返事を」を入れないようにするには
#word1, word2を文字列に変換する-> append
#re.subのoption(1回目だけ消すとか) re.sub(pattern. count)

#[verb, [particle], [noun], [word1, '', word2, '']]
for i in frame:
    if len(i) == 4:
        if len(i[1]) == 0:
            continue
        elif len(i[2]) == 0:
            continue
        else:
#            i[1].sort()
            print "".join(i[2])+i[0], '\t', " ".join(i[1]), '\t', "".join(i[3])
            """
            for j in i[2]:
                for k in i[3]:
                    if i == k:
                        continue
                    else:
                        print k,
            print '\n'.strip()
            """
#            length = len(i[3])
#            print length
#            for j in i[3][0:length-4]:
#                print j,
#            print '\n'.strip()
#"".join(i[3])

f.close()
fw.close()

