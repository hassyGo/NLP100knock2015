# !/usr/bin/python
# coding:UTF-8
# 4-(41)copycopy

import sys
import re
import exp40

class Chunk:
    def __init__(self, line, phrase):
        line = re.sub(r"D", "", line)
        line = line.split()
        self.dst = line[2]
        self.morphs = []
        
        if line[2] not in phrase:
            phrase[line[2]] = [line[1]]
        else:
            phrase[line[2]].append(line[1])
        if line[1] in phrase:
            self.srcs = phrase[line[1]]
        else:
            self.srcs = "none"        

def make_chunk_list(document):
    sentences = []
    sentence = []
    phrase = {}

    for line in document:
        line = line.strip()
        match = exp40.search_sentence(line)

        if line == 'EOS':
            sentences.append(sentence)
            sentence = []
            phrase = {}
        elif match:
            c = Chunk(line, phrase)
            sentence.append(c)
        else:
            sentence[-1].morphs.append(exp40.Morph(line))

    return sentences

#def main():
#と定義すると他のファイルからもmain関数全部を実行することができるようになる    
#if __name__ ...よりはmain()を用いるほうが良いらしい

if __name__ == '__main__':
    main()
    fw = open('41copy.txt', 'w')
    sys.stdout = fw

    document = exp40.read('neko.txt.cabocha')
    sentences = make_chunk_list(document)

    for i in sentences[2]:
        print "dst =", i.dst
        print "srcs =", i.srcs
        for j in i.morphs:
            print j.surface, j.base, j.pos, j.pos1
            
    fw.close()
