#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
token = sent.split(" ")
res = []

for tok in token:
    if len(tok) > 4:
        tmp = list(tok)
        tmp2 = tmp[1:len(tmp)-1]
        random.shuffle(tmp2)
        tmp = "".join(tmp2)
        tok = tok[0]+tmp+tok[-1]
    res.append(tok)

print res

