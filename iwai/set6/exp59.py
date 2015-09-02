# !/usr/bin/python
# coding:UTF-8
# 6-(59): S式の解析
#Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import re
import sys
import exp50
import exp57

if __name__ == "__main__":
    fw = open('59.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    collapsed_dependencies = exp57.make_collapsed_dependencies(document)

    for line in collapsed_dependencies[0]:
        print line
        
    fw.close()
