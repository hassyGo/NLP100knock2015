# !/usr/bin/python
# coding:UTF-8
# 1-(7)

import sys

argv = sys.argv
argc = len(argv)
if (argc != 4):
    print "Error!"

x = int(argv[1])
y = str(argv[2])
z = int(argv[3])

#text = "" 一行でprintすることも可能

print x,
print u"時の",
print y,
print u"は",
print z

#print argv
#pythonでも%d, %s, %.1fも使える
