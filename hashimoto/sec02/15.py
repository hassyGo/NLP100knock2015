#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
N = int(sys.argv[2])

lines = []
#lines = f.readlines()
for line in f:
    line = line.rstrip()
    lines.append(line)
f.close()
for i in range(len(lines)):
    if i >= len(lines)-N:
        print lines[i]
# lines[-N:]
#for i in lines[-N:]:
