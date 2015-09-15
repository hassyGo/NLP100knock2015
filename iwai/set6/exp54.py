# !/usr/bin/python
# coding:UTF-8
# 6-(54):品詞タグ付け
#Stanford Core NLPの解析結果XMLを読み込み，単語(word)，レンマ(lenma)，品詞(POS)をタブ区切り形式で出力せよ．

import re
import sys
import exp50

def main():
    fw = open('54.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    
    for line in document:
        search1 = re.search('<word>(\w+)</word>', line)
        search2 = re.search('<lemma>(\w+)</lemma>', line)
        search3 = re.search('<POS>(\w+)</POS>', line)

        if search1:
            print search1.group(1), '\t',
        if search2:
            print search2.group(1), '\t',
        if search3:
            print search3.group(1)
        
    fw.close()
    
if __name__ == "__main__":
    main()
    
