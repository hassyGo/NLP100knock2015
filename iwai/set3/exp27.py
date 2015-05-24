# !/usr/bin/python
# coding:UTF-8
# 3-(27)

import sys
import re
#import codecs

f = open("write.txt", "r")
fw = open("27.txt", "w")
sys.stdout = fw

lst = []
name = []
#d = {}
d_all = {}
k = 0
cnt = 0

for line in f.readlines():
#     d = {}
     s1 = re.search("^\{\{基礎情報\s国", line)
     s2 = re.search("^\}\}", line)
     if s1:
          d = {}
          k = 1
     if s2:
          k = 0
          d_all[nat]= d
          cnt += 1
     if k == 1:
#          print cnt
          line = line.strip()
          str = re.search("^\|.*\=.*", line)
          name = re.search("^\|略名.*\=", line)
          if name:
               copy = line
               copy = copy.split("=")
               nat = copy[1]
          if str:
               line = line.replace("|", "")
               line = line.replace("'", "")
               line = line.replace("[", "")
               line = line.replace("]", "")
               line = line.split("=")
               d[line[0]] = line[1]

for key, value in d_all.iteritems():
     print "[[[key=",
     print key
     for i,j in value.iteritems():
          print "{",
          print i,j,
          print "}",
     print "]]"

f.close()
fw.close()
