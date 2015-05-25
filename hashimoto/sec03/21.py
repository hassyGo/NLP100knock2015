#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json

for line in sys.stdin:
    wiki = json.loads(line)
    if "title" in wiki:
        if wiki["title"] == u"イギリス":
            kiji = wiki["text"].encode("utf-8")

kiji = kiji.split("\n")

for line in kiji:
    if "[[Category" in line:
        print line
