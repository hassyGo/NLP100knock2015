# !/usr/bin/python
# coding:UTF-8
# 4-(47)copy

import sys
import re
import exp40
import exp41

if __name__ == '__main__':
    fw = open("47copy.txt", "w")
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = exp41.make_chunk_list(document)

    VP = []
    particle = []
    word = []
    noun = []
    frame = []
    
    for i in sentences:
        flag = 0
        p1 = 0
        p2 = 0
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
                            elif m.pos1 == 'サ変接続':
                                p1 = 1
                            else:
                                word.append(m.surface)
                            if p1 == 1:
                                for n in i[int(k)].morphs:
                                    noun.append(n.surface)
                                if len(particle) == 0:
                                    continue
                                else:
                                    particle.pop()
                                    p1 = 0
                    word.append(" ")
                    flag = 0
                VP.append(particle)
                if 'を' in noun:        
                    VP.append(noun)
                for item1 in noun:
                    for item2 in word:
                        if item1 == item2:
                            word.remove(item2)
                VP.append(word)
                particle = []
                word = []
                noun = []
                frame.append(VP)

    for i in frame:
        if len(i) == 4:
            if len(i[1]) == 0:
                continue
            elif len(i[2]) == 0:
                continue
            else:
                print "".join(i[2])+i[0], '\t', " ".join(i[1]), '\t', "".join(i[3])

    fw.close()

