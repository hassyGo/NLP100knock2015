# !/usr/bin/python
# coding:UTF-8
# 4-(40)のcopy, defとか使って編集したver.

import sys
import re

class Morph:
    def __init__(self, line):
        line = line.split("\t")
        self.surface = line[0]
        word = line[1].split(",")
        self.base = word[6]
        self.pos = word[0]
        self.pos1 = word[1]

def read(filename):
    lst = []
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip()
        lst.append(line)

    f.close()

    return lst

def search_sentence(line):
    r = re.compile("\*")
    match = r.match(line)
    
    return match
    
if __name__ == "__main__":
    fw = open("40.txt", "w")
    sys.stdout = fw

    subset = []
    all = []

    document = read('neko.txt.cabocha')
    
    for line in document:
        match = search_sentence(line)
        
        if line == "EOS":
            all.append(subset)
            subset = []
        elif match:
            continue
        else:
            subset.append(Morph(line))

    for i in all[5]:
        print i.surface, i.base, i.pos, i.pos1

    fw.close()

