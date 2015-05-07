#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
token = s.split(" ")

for tok in token:
    count = 0
    for i in range(0, len(tok)): # 0, がいらない
        if tok[i].isalpha():
            count += 1
    sys.stdout.write(str(count))
print 
