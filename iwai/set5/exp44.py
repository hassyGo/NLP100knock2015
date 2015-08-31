# !/usr/bin/python
# coding:UTF-8
# 4-(44)copy

import sys
import re
import exp40
import exp41
import exp42

if __name__ == '__main__':
    fw = open("44.dot", "w")
    sys.stdout = fw

    argv = sys.argv
    argc = len(argv)
    
    n = int(sys.argv[1])

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)

    pairs = []
    test = []
    
    for i in sentences:
        for j in i:
            if j.srcs == 'none':
                continue
            else:
                for k in j.srcs:
                    a = i[int(k)].morphs
                    b = j.morphs
                    pair = a,b
                    pairs.append(pair)
        test.append(pairs)
        pairs = []
        
    print 'digraph sample{'
    print '', 'graph [rankdir = LR];'
    for i in test[n]:
        for j in i[0]:
            sys.stdout.write(j.surface)
        print '->',
        for j in i[1]:
            sys.stdout.write(j.surface)
        print '\n'.strip()
    print '}'

    fw.close()

