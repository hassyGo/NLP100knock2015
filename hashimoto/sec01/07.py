#!/usr/bin/env python
# -*- coding: utf-8 -*-

def temp(x, y, z):
    return str(x)+"時の"+str(y)+"は"+str(z) #フォーマット指定でprintfみたいに書ける XX % (引数)

print temp(12, "気温", 22.4)
