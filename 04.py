#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
token = s.split(" ")
candidate = [1, 5, 6, 7, 8, 9, 15, 16, 19]
mp = {}

for i in range(0, len(token)):
    if i+1 in candidate:
        mp[token[i][0]] = i+1
    else:
        mp[token[i][:2]] = i+1

print mp
