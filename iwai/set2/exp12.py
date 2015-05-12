# !/usr/bin/python
# coding:UTF-8
# 2-(12)

f = open("hightemp.txt", "r")
fw1 = open("col1.txt", "w")
fw2 = open("col2.txt", "w")

for line in f.readlines():
    line = line.split("\t")
    Fir = line[0]
    Sec = line[1]
    fw1.write(Fir + "\n")
    fw2.write(Sec + "\n")

f.close()
fw1.close()
fw2.close()
