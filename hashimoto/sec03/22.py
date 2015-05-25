#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, re

for line in sys.stdin:
    wiki = json.loads(line)
    if "title" in wiki:
        if wiki["title"] == u"イギリス":
            kiji = wiki["text"].encode("utf-8")

kiji = kiji.split("\n")

for line in kiji:
    if "[[Category" in line:
        beg = re.compile(":")
        end = re.compile("\||]")
        m1 = beg.search(line, 0)
        m2 = end.search(line, 0)
        print line[m1.start()+1:m2.end()-1]
