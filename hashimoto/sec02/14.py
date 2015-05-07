#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
N = int(sys.argv[2])

count = 0

for line in f:
    if count < N:
        line = line.rstrip()
        print line
        count += 1
    else:
        break
