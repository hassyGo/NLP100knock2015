#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _30 import kaiseki

sentences = kaiseki()
baseSet = set()

for s in sentences:
    for keitaiso in s:
        baseSet.add(keitaiso["base"])

for base in baseSet:
    print base
