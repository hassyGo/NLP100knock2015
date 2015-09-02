# !/usr/bin/python
# coding:UTF-8
# 6-(51):単語の切り出し
#空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

import re
import sys
import exp50

if __name__ == "__main__":
    fw = open('51.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt')
    
    for line in document:
        string = re.sub('\s', '\n', line)
        search = re.search('\w+\.', string)
        if search:
            print string
            print '\n'.strip()
        else:
            print string    

    fw.close()
