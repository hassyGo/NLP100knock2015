# !/usr/bin/python
# coding:UTF-8
# 1-(9)

import re
import sys
import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

s1 = str.split()
num1 = len(s1)
cnt = 1
shuff = [""]* num1
sub = []

if num1 <= 4:
    print s1
else:
    for i in range(num1):
        if cnt == 1 or cnt == num1:
            shuff[i] = s1[i]
            cnt += 1
        else:
            sub.append(s1[i])
            cnt += 1

random.shuffle(sub)

for i in range(num1):
    if len(shuff[i]) == 0:
        shuff[i] = sub[i-1]

print shuff


#list[1:-1]を使うと早い気がする
#最初と最後以外をシャッフルするようにする
