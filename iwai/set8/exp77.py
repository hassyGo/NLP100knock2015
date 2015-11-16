# !usr/bin/python
# coding:UTF-8
#(77)正解率の計測
#76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import sys
import random
import string
import nltk
import exp70


def main():
    result = exp70.read('76.txt')
    TP, TN, FP, FN = 0, 0, 0, 0
    
    for line in result:
        line = line.split()
        if line[0] == line[1]:
            if line[0] == '1':
                TP += 1
            else:
                TN += 1
        else:
            if line[0] == '1':
                FP += 1
            else:
                FN += 1

    #予測の正解率 = (TP + TN) / (TP + TN + FP + FN)
    accuracy = 1.0 * (TP + TN) / (TP + TN + FP + FN)
    print 'accuracy:', accuracy

    #正例の適合率 = TP / (TP + FP)
    precision = 1.0 * TP / (TP + FP)
    print 'precision:', precision

    #再現率 = TP / (TP + NP)
    recall = 1.0 * TP / (TP + FN)
    print 'recall:', recall

    #f_score = 2 * recall * precision / (recall + precision)
    f = 2.0 * (recall * precision) / (recall + precision)
    print 'f_score:', f

    
if __name__ == '__main__':
    main()
    
        
