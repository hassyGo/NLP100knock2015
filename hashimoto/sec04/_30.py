#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kaiseki():
    f = open("./neko.txt.mecab")
    sentences = []
    s = []

    for line in f:
        line = line.rstrip()
    
        if line == "EOS":
            sentences.append(s)
            s = []
            continue
    
        keitaiso = {}
        lst1 = line.split("\t")
        lst2 = lst1[1].split(",")
        keitaiso["surface"] = lst1[0]
        keitaiso["base"] = lst2[6]
        keitaiso["pos"] = lst2[0]
        keitaiso["pos1"] = lst2[1]
        s.append(keitaiso)
        
    f.close()
    return sentences
