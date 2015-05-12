# !/usr/bin/python
# coding:UTF-8
# 2-(14)

import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print "Error!"

n = int(sys.argv[1])

f = open("hightemp.txt", "r")
line = f.readlines()

for num in range(0,n):
    print line[num],

f.close()
