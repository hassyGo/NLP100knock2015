#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
youso = []

for line in f:
    line = line.rstrip()
    youso.append(line.split("\t"))

youso.sort(cmp=lambda x,y: cmp(float(y[2]), float(x[2])))

for y in youso:
    print y[0]+"\t"+y[1]+"\t"+y[2]+"\t"+y[3]
