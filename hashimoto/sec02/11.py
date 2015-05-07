#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

fileName = sys.argv[1]
f = open(fileName)

for line in f:
    line = line.strip()
    line = line.replace("\t", " ")
    print line
