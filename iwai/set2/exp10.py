# !/usr/bin/python
# coding:UTF-8
# 2-(10)

f = open("hightemp.txt", "r")
cnt = 0

for line in f.readlines():
    cnt += 1

print cnt

f.close()
