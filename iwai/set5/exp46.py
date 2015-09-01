# !/usr/bin/python
# coding:UTF-8
# 4-(46)copy

import sys
import re
import exp40
import exp41

def main():
    fw = open("46.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)
    
    frame = []
    VP = []
    particle = []
    word = []

    for i in sentences:
        flag = 0
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
                            flag = 1
                            break
                    if flag == 1:
                        for m in i[int(k)].morphs:
                            if m.pos == '記号':
                                continue
                            else:
                                word.append(m.surface)
                    word.append(" ")
                    flag = 0
                VP.append(particle)
                VP.append(word)
                particle = []
                word = []
                frame.append(VP)

    for i in frame:
        if len(i) == 3:
            if len(i[1]) == 0:
                continue
            else:
                i[1].sort()
                print i[0], '\t', " ".join(i[1]), '\t', "".join(i[2])

    fw.close()

if __name__ == '__main__':
    main()
