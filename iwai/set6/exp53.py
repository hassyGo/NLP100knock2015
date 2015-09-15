# !/usr/bin/python
# coding:UTF-8
# 6-(53):Tokenization
#Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

import re
import sys
import exp50

def main():
    fw = open('53.txt', 'w')
    sys.stdout = fw
    
    document = exp50.read('50.txt.xml')
    
    for line in document:
        search = re.search('<word>(.+)</word>', line)

        if search:
            print search.group(1)

    fw.close()
    
if __name__ == "__main__":   
    main()
    
