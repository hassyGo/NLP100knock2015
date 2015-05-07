#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

N = len(sys.argv)-2
f = open(sys.argv[1])
ws = []

for i in range(N):
    ws.append(open(sys.argv[2+i], "w"))

index = -1
lines = []

for line in f:
    line = line.rstrip()
    lines.append(line)

STEP = int(len(lines)/N)

for i in range(len(lines)):
    if i % STEP == 0:
        index += 1
    ws[index].write(lines[i]+"\n")

for w in ws:
    w.close()
