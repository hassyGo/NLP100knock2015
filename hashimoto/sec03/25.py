#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, re

for line in sys.stdin:
    wiki = json.loads(line)
    if "title" in wiki:
        if wiki["title"] == u"イギリス":
            kiji = wiki["text"].encode("utf-8")

kiji = kiji.split("\n")
pattern1 = re.compile("\{\{基礎情報")
pattern2 = re.compile("\}\}")
pattern3 = re.compile("\|")
flg = False
res = {}

for line in kiji:
    if ~flg and pattern1.match(line):
        flg = True
    elif flg and pattern2.match(line):
        break
    elif pattern3.match(line): 
        l = pattern3.sub("", line).split(" = ")
        print l[0], l[1]
        res[l[0]] = l[1]
