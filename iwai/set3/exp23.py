# !/usr/bin/python
# coding:UTF-8
# 3-(23)

import sys
import re

f = open("write.txt", "r")
fw = open("23.txt", "w")
sys.stdout = fw

lst = []

for line in f.readlines():
#    print line,
#    s1 = re.search("^\=\=\s.+\s\=\=", line)
    s = re.search("(==+)\s(.+)\s(==+)", line)
    if s:
        line = line.strip()
        print s.group(2),
        print len(s.group(1))-1
#        print s1.group(1)
f.close()
fw.close()
