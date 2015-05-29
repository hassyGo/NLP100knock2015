# !/usr/bin/python
# coding:UTF-8
# 4-(30) new ver.

#[お腹：{表層系：何か},},{}]
#[すい:{},{},{}]
#[た:{},{},{}]

#1文目を実行--> d = {surface: お腹, base:お腹 , pos: 名詞, pos1: 一般}

#形態素のリストとして表現--> [[{surface: お腹, base:お腹 , pos: 名詞, pos1: 一般},{surface: すい, base:すく , pos: 動詞, pos1: 自立},{surface: た, base:た , pos: 助動詞, pos1: *}],[]]

import sys
import re
import copy

f = open("neko.txt.mecab", "r")
fw = open("write_new.txt", "w")
sys.stdout = fw

all = []
subset = []
k = 0
cnt = 0

for line in f.readlines():
    d = {}
#    subset = []
    line = line.strip()
    if line == "EOS":
        all.append(copy.copy(subset))
#        cnt += 1
#        all.append(subset)
#        print all
        del subset[:]
    else:
#        subset = []
        line = line.split("\t")
        fir = line[0]
        sec = line[1]
        d['surface'] = line[0]
#        print d.items()
#        print fir
        sec = sec.split(",")
        d['base'] = sec[6]
        d['pos'] = sec[0]
        d['pos1'] = sec[1]
        subset.append(d)

for i in all:
    print "[",
    for j in i:
        for key, value in j.items():
            print "{",
            print key,
            print ":",
            print value,
            print "}",
    print "]"

f.close()
fw.close()
