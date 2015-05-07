#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
field1 = []

for line in f:
    field1.append(line.split("\t")[0])

result = set(field1)
print len(result)
