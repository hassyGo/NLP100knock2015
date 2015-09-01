# !/usr/bin/python
# coding:UTF-8
# 4-(45)copy

import sys
import re
import exp40
import exp41

def main():
    fw = open("45copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)

    particle = []
    frame = []
    VP = []
    
    for i in sentences:
        for j in i:
            if j.srcs == 'none':
                continue
            else:
                VP = []
                for k in j.morphs:
                    if k.pos == '動詞':
                        VP.append(k.base)
                        break
                for k in j.srcs:
                    for l in i[int(k)].morphs[::-1]:
                        if l.pos == '助詞':
                            particle.append(l.surface)
                            break
                VP.append(particle)
                particle = []
                frame.append(VP)

    for i in frame:
        if len(i) == 2:
            if len(i[1]) == 0:
                continue
            else:
                i[1].sort()
                print i[0], '\t', " ".join(i[1])


    fw.close()

if __name__ == '__main__':
    main()
