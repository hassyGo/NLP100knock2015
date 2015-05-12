# !/usr/bin/python
# coding:UTF-8
# 1-(5)
 
def n_gram(uni,n):
    return [uni[k:k+n] for k in range(len(uni)-n+1)]

def ngram_word(bai, n):
    s1 = bai.split()
    return [s1[k:k+n] for k in range(len(s1)-n+1)]

str = n_gram('I am an NLPer', 2)
print "文字バイグラム:",
print str

word = ngram_word('I am an NLPer', 2)
print "単語バイグラム:",
print word

#from itertools import chain

