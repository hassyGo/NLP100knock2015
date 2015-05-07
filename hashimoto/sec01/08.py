#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(s):
    sl = list(s)
    for i in range(0, len(sl)):
        if sl[i].islower(): # 正規表現を遣え
            sl[i] = unichr(219-ord(s[i]))
    return "".join(sl)

def hukugou(s):
    sl = list(s)
    for i in range(0, len(sl)):
        if ord(sl[i]) >= 219-ord("z") and ord(sl[i]) <= 219-ord("a"):
            sl[i] = unichr(219-ord(sl[i]))
    return "".join(sl)

s = "tEsT"
print s
print cipher(s)
print hukugou(cipher(s))
