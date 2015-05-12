# !/usr/bin/python
# coding:UTF-8
# 2-(11)

f = open("hightemp.txt", "r")

for line in f.readlines():
    s = line.replace("\t", " ")
    print s,

f.close()

#readlines()とreadline()の違い
