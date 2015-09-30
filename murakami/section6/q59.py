#!/usr/bin/env python
#coding: utf-8

"""
    59. S式の解析
    Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""

from q53 import *
import re

#nltkを使え

def getSubtreeString(dic,wordlist,subroot):
    strings = []
    visited = [subroot]
    stack = [subroot]
    while len(stack) > 0:
        v = stack.pop()
        
        if len(dic[v]) == 0:
            strings.append(wordlist[int(v)])
        for i in dic[v][::-1]:
            if (i in visited) == False:
                visited.append(i)
                stack.append(i)

    return " ".join(strings)


def lispParser(lisp):
    string = re.sub(r'[a-zA-Z0-9\`\'$\?:,\.\-]+',"node",lisp)
    
    wordlist = filter(lambda w: len(w) > 0, re.split(r'[\s\(\)]', lisp))
    
    dic = {}
    
    count = 0
    while True:
        a = string.find("node")
        if a < 0:break
        string = string.replace("node",str(count),1)
        dic[str(count)] = []
        count += 1

    print string

    while True:
        b = re.search(r'\([^\(\)]*\)',string)
        if b == None:
            break
        words = filter(lambda w: len(w) > 0, re.split(r'[\s\(\)]', b.group()))
        dic[words[0]].extend(words[1:])
        string = string[0:b.start()] + words[0] + string[b.end():]
        print string

    print dic

    #ここから深さ優先探索
    visited = ["0"]
    stack = ["0"]
    while len(stack) > 0:
        v = stack.pop()
        if wordlist[int(v)] == "NP":
            print getSubtreeString(dic,wordlist,v)
        for i in dic[v][::-1]:
            if (i in visited) == False:
                visited.append(i)
                stack.append(i)



if __name__ == "__main__":
    root = readXml("nlp.txt.xml") #xmlから木構造を作る

    for sentences in root.iter("sentences"):
        for sentence in sentences.iter("sentence"):
            lispParser(sentence.find("parse").text)
