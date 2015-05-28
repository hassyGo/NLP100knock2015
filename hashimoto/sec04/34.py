#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _30 import kaiseki

sentences = kaiseki()
npSet = set()

for s in sentences:
    for i in range(len(s)-2):
        if s[i]["pos"] == "名詞" and s[i+1]["surface"] == "の" and s[i+2]["pos"] == "名詞":
            npSet.add(s[i]["surface"]+s[i+1]["surface"]+s[i+2]["surface"])

for np in npSet:
    print np
