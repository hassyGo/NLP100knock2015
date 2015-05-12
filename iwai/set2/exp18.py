# !/usr/bin/python
# coding : UTF-8
# 2-(18)

f = open("hightemp.txt", "r")
lst =[]

for line in f.readlines():
    line = line.strip()
    line = line.split("\t")
    fir = line[0]
    sec = line[1]
    thi = line[2]
#    print thi
    lst.append([fir, sec, thi])

lst.sort(lambda b,c: cmp(b[2], c[2]), reverse = True)
"""
for i in lst:
    print i[0],
    print i[1],
    print i[2]
"""

#lambdaだけでもいける
