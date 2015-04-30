#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(seq, n, res):
    for i in range(0, len(seq)):
        if i+n-1 < len(seq):
            res.append(seq[i:i+n])

s1 = "paraparaparadise"
s2 = "paragraph"

X = []
Y = []

ngram(s1, 2, X)
ngram(s2, 2, Y)
X = set(X)
Y = set(Y)

Wa = X.union(Y)
Seki = X.intersection(Y)
Sa1 = X.difference(Y)
Sa2 = Y.difference(X)

print Wa
print Seki
print Sa1
print Sa2
print X.issuperset(["se"])
print Y.issuperset(["se"])
