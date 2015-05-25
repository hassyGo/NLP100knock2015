#!/usr/bin/env python
#coding: utf-8

"""
    24. ファイル参照の抽出
    記事から参照されているメディアファイルをすべて抜き出せ．
"""

import json
import string
import re

import q20


if __name__ == "__main__":
    jsonData = q20.readJson("england.json")[0]
    text = jsonData["text"]

    for m in re.finditer(u'\[\[ファイル:.*\]\]',text):
        print m.group()