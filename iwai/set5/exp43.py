# !/usr/bin/python
# coding:UTF-8
# 4-(43)copy

import sys
import re
import exp40
import exp41
import exp42

if __name__ == '__main__':
    fw = open("43copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)
    make_pairs = exp42.make_chunk_pairs(sentences)

    for i in make_pairs:
        k1 = 0
        k2 = 0
        for j in i[0]:
            if j.pos == '記号':
                continue
            else:
                if j.pos == '名詞':
                    k1 = 1
                    break
        for j in i[1]:
            if j.pos == '記号':
                continue
            else:
                if j.pos == '動詞':
                    k2 = 1
                    break
        if k1 == 1 and k2 == 1:
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

