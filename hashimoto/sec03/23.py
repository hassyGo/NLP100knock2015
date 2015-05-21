#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, re

for line in sys.stdin:
    wiki = json.loads(line)
    if "title" in wiki:
        if wiki["title"] == u"イギリス":
            kiji = wiki["text"].encode("utf-8")

kiji = kiji.split("\n")
pattern = re.compile("=+.*=+")

for line in kiji:
    if pattern.match(line):
        print line,
        print line.count("=")/2-1
