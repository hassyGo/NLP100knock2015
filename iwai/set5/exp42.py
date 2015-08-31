# !/usr/bin/python
# coding:UTF-8
# 4-(42)copy

import sys
import re
import exp40
import exp41

def make_chunk_pairs(sentences):
    pairs = []
    
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

    return pairs

if __name__ == '__main__':
    fw = open("42_copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)
    chunk_pairs = make_chunk_pairs(sentences)
    
    for i in chunk_pairs:
        for j in i[0]:
            if j.pos == '記号':
                continue
            else:
                sys.stdout.write(j.surface)
        print '\t',
        for j in i[1]:
            if j.pos == '記号':
                continue
            else:
                sys.stdout.write(j.surface)
        print '\n'.strip()

    fw.close()

