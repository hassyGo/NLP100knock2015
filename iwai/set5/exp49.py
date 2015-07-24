# !/usr/bin/python
# coding:UTF-8
# 4-(49)

import sys
import re

f = open("ichi.txt", "r")
fw = open("49.txt", "w")
sys.stdout = fw

subset = []
all = []
chunks = []
sentence = []
phrase = {0:[0]}
#pair1 = []
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

for sentence in all: 
    flag1 = 0
    CNT = 0
    length = len(sentence)-1
    for chunk in sentence:
        cnt = CNT
        X_chunk = []
        X_dst = []
        #X, Yのpairを作る
        #(Xのchunk,Yのchunk)
        for morph in chunk.morphs:
            if morph.pos == '名詞' and chunk not in X_chunk:
                X_chunk.append(chunk)
                n = int(chunk.dst)
#                print n
                while n != -1:
                    X_dst.append(n)
                    n = int(sentence[n].dst)
                flag1 = 1
        if flag1 == 1:
            Y_chunk = []
            while length != cnt:
                Y_chunk = list(X_chunk)
                Y_dst = []
                for morph in sentence[cnt+1].morphs:
                    if morph.pos == '名詞' and sentence[cnt+1] not in Y_chunk:
                        #pattern Aのとき
                        if cnt+1 in X_dst:
                            for i in X_dst:
                                if i != cnt+1:
                                    Y_chunk.append(' -> ')
                                    Y_chunk.append(sentence[i])
                                else:
                                    Y_chunk.append(' -> ')
                                    Y_chunk.append(sentence[cnt+1])
                                    break
                        #pattern Bのとき
                        else:
                            Y_chunk.append(' | ')
                            Y_chunk.append(sentence[cnt+1])
                            n = int(sentence[cnt+1].dst)
#                            print n
                            while n != -1:
                                Y_dst.append(n)
                                n = int(sentence[n].dst)
                            X_dst_set = set(X_dst)
                            test = X_dst_set.intersection(Y_dst)
                            for i in Y_dst:
                                if i == list(test)[0]:
                                    break
                                else:
                                    Y_chunk.append(' -> ')
                                    Y_chunk.append(sentence[i])
#                            print list(test)[0]
#                            while cnt+1 != list(test)[0]:
                                
#                            Y_chunk.append(sentence[cnt+1])
                            Y_chunk.append(' | ')
                            Y_chunk.append(sentence[list(test)[0]])
                        pairs.append(Y_chunk)

                cnt += 1
                Y_chunk = []
        flag1 = 0
        CNT += 1
        X_dst = []

#pairs = [[X,Y],[X,Y]...[X,Y]]
#pairsの中身を表示するには->

for pair in pairs:
#    print pair
    for chunk in pair:
        if type(chunk) == str:
            print chunk,
        else:
            for morph in chunk.morphs:
                sys.stdout.write(morph.surface)
    print '\n'.strip()

"""
for pair in pairs:
    print pair

#    X_dst = []
#    n = int(pair[0].dst)
#    print n
#    while n != -1:
        
#   for chunk in pair[0]:
#        print chunk
#    X_dst.append(pair[0].dst)
#    for chunk in pair[0]:
#      print 'X_chunkがもつdst', chunk.dst  
"""
f.close()
fw.close()


