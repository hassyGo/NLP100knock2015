# !/usr/bin/python
# coding:UTF-8
# 1-(6)

def n_gram(uni,n):
    return [uni[k:k+n] for k in range(len(uni)-n+1)]

s1 = []
s2 = []

s1 = n_gram('paraparaparadise', 2)
s2 = n_gram('paragraph', 2)
#print s1
#print s2

inter = set(s1).intersection(set(s2))
print "積集合",
print inter

uni = set(s1).union(set(s2))
print "和集合",
print uni

diff = set(s1).difference(set(s2))
print "積集合",
print diff

#import file名(.pyを除く)as 関数名
#
