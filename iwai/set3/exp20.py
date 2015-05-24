# !/usr/bin/python
# coding:UTF-8
# 3-(20)

import sys
import re

f = open("jawiki-country.json", "r")
fw = open("write.txt", "w")
sys.stdout = fw

lst = []

for line in f.readlines():
    s = re.search(r"イギリス", line)
    if s:
#        print "poge"
        lst.append(line)

#for i in lst:
#    print i
#print lst

#改行コードを表示するとき
for i in lst:
    i = i.replace(r"\n", "\n")
    print i

f.close()
fw.close()
