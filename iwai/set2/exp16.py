# !/usr/bin/python
# coding:UTF-8
# 2-(16)

import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print "Error!"

n = int(sys.argv[1])

f = open("hightemp.txt", "r")
lst = []
sub = []

num = 24 / n

print num
for line in f.readlines():
    lst.append(line)

for i in lst:
    sub.append(i)
    if len(sub) == num:
        for j in sub:
            print j,
        print "\n".strip()
        del sub[:]
#print zip(*[iter(lst)]*3)
