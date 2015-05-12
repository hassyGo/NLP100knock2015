# !/usr/bin/python
# coding:UTF-8
# 2-(15)

import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print "Error!"

n = int(sys.argv[1])

f = open("hightemp.txt", "r")
line = f.readlines()

tail = 24 - n

for num in range(tail,24):
    print line[num],

f.close()


#行数を獲得する　--> cnt回してcount
#len(line)で獲得
#lines[-n:]だと後ろから出力できる
#for i in lst[-n:]
#  print i
