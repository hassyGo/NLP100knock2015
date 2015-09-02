# !/usr/bin/python
# coding:UTF-8
# 6-(55):固有表現抽出
#入力文中の人名をすべて抜き出せ．

import re
import sys
import exp50

if __name__ == "__main__":
    fw = open('55.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    sentence = []
    flag = 0
    
    for line in document:
        search1 = re.search('<token id=".+">', line)
        search2 = re.search('</token>', line)
        if search1:
            word = []
            flag = 1
        if search2:
            sentence.append(word)
            flag = 0
        if flag == 1:
            word.append(line)

    for word in sentence:
        if '<NER>PERSON</NER>' in word:
            search3 = re.search('<word>(\w+)</word>', word[1])
            if search3:
                print search3.group(1)
        
    fw.close()
