# !/usr/bin/python
# coding:UTF-8
# 6-(52):ステミング
#51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

import re
import sys
import nltk
import exp50

def main():
    fw = open('52.txt', 'w')
    sys.stdout = fw
    stemmer = nltk.PorterStemmer()

    document = exp50.read('51.txt')
    
    for line in document:
        print line, '\t', stemmer.stem(line)

    fw.close()
    
if __name__ == "__main__":
    main()
    
