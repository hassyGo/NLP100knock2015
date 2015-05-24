# !/usr/bin/python
# coding:UTF-8
# 3-(24)

import sys
import re

f = open("write.txt", "r")
fw = open("24.txt", "w")
sys.stdout = fw

lst = []

for line in f.readlines():
#    print line,
#    s1 = re.search("^\[\[ファイル:(.+?\..{1,3})|^\[\[File:(.+?\..{1,3})", line)
    s1 = re.search("^\[\[ファイル:(.+?\..{1,3})", line)
    s2 = re.search("^\[\[File:(.+?\..{1,3})", line)
    if s1:
#        print line,
        print s1.group(1)
    if s2:
#        print line,
        print s2.group(1)

f.close()
fw.close()
