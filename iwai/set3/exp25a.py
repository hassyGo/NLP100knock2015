# !/usr/bin/python
# coding:UTF-8
# 3-(25)a

import sys
import re

f = open("write.txt", "r")
fw = open("25a.txt", "w")
sys.stdout = fw

lst = []
k = 0

for line in f.readlines():
#    line = line.encode("utf-8")
#    print line,
    s1 = re.search("\{\{基礎情報", line)
    s2 = re.search("^\}\}$", line)
    if s1:
        k = 1
#        print "\n",

    if s2:
        k = 0
##        print "finish"

    if k == 1:
        line = line.strip()
#        print line,
        name = re.search("^\|略名.*\=\s?(.+)", line)
        if name:
            print type(name.group())
#            print line
#            print name.group(0)
            print name.group(1)
            
"""
               copy = line
               copy = copy.split("=")
               nat = copy[1]
          if str:
               line = line.replace("|", "")
               line = line.split("=")
               d[line[0]] = line[1]
#        lst.append(line)
"""
f.close()
fw.close()
