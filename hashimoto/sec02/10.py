#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

fileName = sys.argv[1]
f = open(fileName)
count = 0

for line in f:
#    line = line.rstrip()
#    print line
    count += 1

print count
