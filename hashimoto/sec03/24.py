#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, re

for line in sys.stdin:
    wiki = json.loads(line)
    if "title" in wiki:
        if wiki["title"] == u"イギリス":
            kiji = wiki["text"].encode("utf-8")

kiji = kiji.split("\n")
pattern1 = re.compile("\[\[ファイル:|\[\[File:")
pattern2 = re.compile(":")
pattern3 = re.compile("\||]")

for line in kiji:
    m = pattern1.search(line, 0)
    if m:
        print line[pattern2.search(line, 0).start()+1:pattern3.search(line, 0).end()-1]
