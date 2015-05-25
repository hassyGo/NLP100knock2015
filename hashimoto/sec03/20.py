#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json

def extract(name):
    for line in sys.stdin:
        wiki = json.loads(line)
        if "title" in wiki:
            if wiki["title"] == name:
                kiji = wiki["text"].encode("utf-8")
    return kiji

print extract(u"イギリス")
