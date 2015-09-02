# !/usr/bin/python
# coding:UTF-8
# 6-(57):かかり受け解析
#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
#.dotの実行方法 -> dot -Tpng 57.dot -o 57.png

import re
import sys
import exp50

def make_collapsed_dependencies(document):    
    sentence = []
    sentences = []
    flag = 0
    
    for line in document:
        if line == '<collapsed-dependencies>':
            flag = 1
        if line == '</collapsed-dependencies>':
            sentences.append(sentence)
            flag = 0
            sentence = []
        if flag == 1:
            sentence.append(line)

    return sentences

def search_governor(line):
    match = re.match('<governor idx=".+">(\w+)</governor>', line)
    if match:
        return  match.group(1)

def search_dependent(line):
    match = re.match('<dependent idx=".+">(\w+)</dependent>', line)
    if match:
        return match.group(1)
    
def main():
    fw = open('57.dot', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    collapsed_dependencies = make_collapsed_dependencies(document)
    
    print 'digraph sample{'
    print '', 'graph [rankdir = LR];'

    for line in collapsed_dependencies[2]:
        governor = search_governor(line)
        dependent = search_dependent(line)

        if governor != None:
            print governor, '->',
        if dependent != None:
            print dependent
    print '}'
    
    fw.close()
    
if __name__ == "__main__":
    main()
    
