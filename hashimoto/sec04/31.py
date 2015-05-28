#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _30 import kaiseki

sentences = kaiseki()
surfaceSet = set()

for s in sentences:
    for keitaiso in s:
        surfaceSet.add(keitaiso["surface"])

for surface in surfaceSet:
    print surface
