# !/usr/bin/python
# coding:UTF-8
# (70)文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ
#rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
#rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
#上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
#sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import sys
import random
import string
import nltk

def read(filename):
    lst = []
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip()
        line = filter(lambda x: x in string.printable, line)
        lst.append(line)

    f.close()

    return lst


def main():
    fw = open('sentiment.txt', 'w')
    sys.stdout = fw
    sentences = []
    #stemmer = nltk.PorterStemmer()
    
    negative_doc = read('rt-polarity.neg')
    positive_doc = read('rt-polarity.pos')
    
    for line in negative_doc:
        
        lst = []
        lst.append('-1')
        lst.append(line)
        sentences.append(' '.join(lst))

    for line in positive_doc:
        lst = []
        lst.append('+1')
        lst.append(line)
        sentences.append(' '.join(lst))

    #sentencesの中身をランダムにする
    random.shuffle(sentences)
    
    for sentence in sentences:
        print sentence


if __name__ == '__main__':
    main()
