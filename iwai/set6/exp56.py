# !/usr/bin/python
# coding:UTF-8
# 6-(56):共参照解析
#Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．


#ElementTreeとitertoolを組み合わせてなんとかやってみる
#村上さんのプログラムを参考に

import re
import sys
import exp50

#coreferenceの部分だけとってきたリストを作る
def make_coreferences(document):
    coreference = []
    coreferences = []
    flag = 0

    for line in document:
        if line == '<coreference>':
            flag = 1
        if line == '</coreference>':
            coreference.append(line)
            coreferences.append(coreference)
            flag = 0
            coreference = []
        if flag == 1:
            coreference.append(line)

    return coreferences

#[文の番号, 単語id, representative mention(mention)]となったリストが詰まったリストを作る
def make_mentions(coreferences):
    word_representative = []
    word = []
    word_lst = []
    flag = 0

    #print coreferences
    
    for coreference in coreferences:
        for item in coreference:
            representative = re.search('<mention representative="true">', item)
            sentence = re.match('<sentence>(\w+)</sentence>', item)
            start = re.match('<start>(\w+)</start>', item)
            text = re.search('<text>(.+)</text>', item)
            mention = re.match('</mention>', item)
            coreference = re.match('</coreference>', item)   

            if representative:
                flag = 1
            if mention:
                flag = 0
                if word_representative:
                    word.append(''.join(word_representative))
                    word_representative = []
            if flag == 1:
                rep_text = re.search('<text>(.+)</text>', item)
                if text:
                    word_representative.append('(')
                    word_representative.append(rep_text.group(1))
                    word_representative.append(')')
                
    return word
          

        
#1文を1リストに変換してsplitして単語レベルに分割したリストにしておく
def make_sentence(filename):
    filename = exp50.read('50.txt')
    lst = []
    
    for line in filename:
        line = line.split()
        lst.append(line)

    return lst
        
    
    
def main(): 
    fw = open('56.txt', 'w')
    sys.stdout = fw

    coreferences = []
    filename = []
    flag = 0
    
    document = exp50.read('nlp_lined_rmHeader.txt.xml')
    sentence_list = make_sentence(filename)
    #print sentence_list
    coreferences = make_coreferences(document)
    mention_list = make_mentions(coreferences)
    print mention_list

    
    fw.close()
   
if __name__ == "__main__":
    main()
