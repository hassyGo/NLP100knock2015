# !/usr/bin/python
# coding:UTF-8
# 1-(3)

import string

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s1 = str.translate(string.maketrans("", ""), ",.")
s2 = s1.split()

lst = []
num = len(s2)
print s2

#print s2
#range(0,num) --> rangeは0がなくてもOK

for i in range(num):
     lst.append(len(s2[i]))
print lst

