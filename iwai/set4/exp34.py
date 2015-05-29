# !/usr/bin/python
# coding:UTF-8
# 4-(34)

import sys
import re
import copy

f = open("neko.txt.mecab", "r")
fw = open("34.txt", "w")
sys.stdout = fw

subset = []
all = []
lst = []

for line in f.readlines():
    d = {}
    line = line.strip()
    if line == "EOS":
        all.append(copy.copy(subset))
        del subset[:]
    else:
        line = line.split("\t")
        fir = line[0]
        sec = line[1]
        d['surface'] = line[0]
        sec = sec.split(",")
        d['base'] = sec[6]
        d['pos'] = sec[0]
        d['pos1'] = sec[1]
        subset.append(d)

for i in all:
    for j in range(len(i)-3):
        lst.append(i[j:j+3])

for i in lst:
#    for j in i:
#        for ley, value in j.items():
#            if value == "pos"
    if i[0]['pos'] == "名詞" and i[1]['surface'] == "の" and i[2]['pos'] == "名詞":
        print i[0]['surface'], i[1]['surface'], i[2]['surface']

"""
for i in lst:
    for j in i:
        for key, value in j.items():
            print key, value,
    print "\n"
"""
"""
for line in f.readlines():
    d = {}
    line = line.strip()
    line = line.replace("EOS", "")
    if line == "":
        continue
    else:
        line = line.split("\t")
        fir = line[0]
        sec = line[1]
        d['surface'] = line[0]
        sec = sec.split(",")
        d['base'] = sec[6]
        d['pos'] = sec[0]
        d['pos1'] = sec[1]
        lst.append(d)

#名詞+助詞+名詞を抜き出す
#"の"の前後が抜き出せたら良い??
#
three = []

for i in lst:
#    print i
#    three = []
    three.append(i)
#    print three
#    print three
    if len(three) == 3:
#        print "hoge"
        print three
        del three[:]
#        for j in three:
#            print j
#    del three[:]
#        print three

for i in lst:
    cnt += 1
    str[cnt] = i

#s = re.search("")

for key, value in str.items():
    for s1, s2 in value.items():
        if value["base"] == 'の' and value["pos"] == '助詞':
            print key, value
#    print "\n"
#        if i["pos"] == '助詞':
#            print i

#for key,value in str.iteritems():
#    print key,value

#for i in lst:
#    print "[",
#    for key, value in i.items():
#        print key,value,
#    print "]"

"""
f.close()
fw.close()
