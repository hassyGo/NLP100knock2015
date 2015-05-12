# !/usr/bin/python
# coding:UTF-8
# 1-(8)

import re
import sys

def cipher(str):
    char_list = list(str)
    num = len(char_list)
    result = []
    for i in range(num):

#compileはあった方がいい

        s1 = re.search("[a-z]+", char_list[i])
        if s1:
            #print "change"
            code = ord(char_list[i])
            #文字コードを取得もしくは確認するには？
            result.append(chr(219 - code))
        else:
            result.append(char_list[i]) 
    return result

test = cipher("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
 
for i in test:
    print i,


#復号対象：219-z から219-aの間になる

##
