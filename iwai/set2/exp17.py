# !/usr/bin/python
# coding:UTF-8
# 2-(17)

f = open("col1.txt", "r")
lst =set()

for line in f.readlines():
#    print line
    lst.add(line)

#print len(lst)

for i in lst:
    print i,
#県名を出力できるようにする
