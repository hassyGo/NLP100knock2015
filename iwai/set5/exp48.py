# !/usr/bin/python
# coding:UTF-8
# 4-(48)copy

import sys
import re
import exp40
import exp41
import exp42

if __name__ == '__main__':
    fw = open("48copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)

    pair = []
    pairs = []
    
    for i in sentences:
        flag1 = 0
        flag2 = 0
        for j in i: 
            if j.dst == '-1':
                continue
            else:
                for k in j.morphs:
                    if k.pos == '名詞':
                        flag1 = 1
                    if flag1 == 1:
                        pair.append(k.surface)
                pair.append(" -> ")
                if flag1 == 1:
                    n = int(j.dst)
                    while n != -1:
                        for morph in i[n].morphs:
                            if morph.pos == '記号':
                                continue
                            else:
                                pair.append(morph.surface)
                        pair.append(" -> ")
                        n = int(i[n].dst)
                flag1 = 0
                pairs.append(pair)
                pair = []

    for i in pairs:
        if len(i) == 1:
            continue
        else:
            i.pop()            
            print "".join(i)

    fw.close()


