#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(seq, n, res):
    for i in range(0, len(seq)):
        if i+n-1 < len(seq):
            res.append(seq[i:i+n])

if __name__ == "__main__":
    test = "I am an NLPer"
    res = []
    ngram(test, 2, res)
    print res
    res = []
    ngram(test.split(" "), 2, res)
    print res
