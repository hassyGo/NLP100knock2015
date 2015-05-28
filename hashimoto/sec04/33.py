#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _30 import kaiseki

sentences = kaiseki()
sahenNounSet = set()

for s in sentences:
    for keitaiso in s:
        if keitaiso["pos"] == "名詞" and keitaiso["pos1"] == "サ変接続":
            sahenNounSet.add(keitaiso["base"])

for sahen in sahenNounSet:
    print sahen
