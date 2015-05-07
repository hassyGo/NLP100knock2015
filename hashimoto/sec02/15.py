#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
N = int(sys.argv[2])

lines = []

for line in f:
    line = line.rstrip()
    lines.append(line)

for i in range(len(lines)):
    if i >= len(lines)-N:
        print lines[i]
