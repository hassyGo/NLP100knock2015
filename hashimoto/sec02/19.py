#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
count = {}

for line in f:
    line = line.rstrip()
    col1 = line.split("\t")[0]
    if col1 in count:
        count[col1] += 1
    else:
        count[col1] = 1

items = count.items()
items.sort(cmp=lambda x,y: cmp(y[1], x[1]))

for item in items:
    print item[0]+"\t"+str(item[1])
