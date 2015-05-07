#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

col1 = open(sys.argv[1])
col2 = open(sys.argv[2])
res = open(sys.argv[3], "w")

results = []

for line in col1:
    line = line.rstrip()
    results.append(line)

count = 0

for line in col2:
    line = line.rstrip()
    if count < len(results):
        results[count] += "\t"+line
    count += 1

for s in results:
    res.write(s+"\n")
