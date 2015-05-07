#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

fileName = sys.argv[1]
f = open(fileName)
f1 = open("col1.txt", "w")
f2 = open("col2.txt", "w")

for line in f:
    line = line.rstrip()
    fields = line.split("\t")
    f1.write(fields[0]+"\n")
    f2.write(fields[1]+"\n")

f1.close()
f2.close()
