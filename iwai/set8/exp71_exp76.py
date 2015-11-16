# !usr/bin/python
# coding:UTF-8

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import sys
import random
import string
import nltk
import exp70
import numpy as np

# (71)ストップワード
#英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
#さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関\数を実装せよ
#さらに，その関数に対するテストを記述せよ．   
def search_stop_word(word):
    stop_word = exp70.read('stop_word.txt')

    return word in stop_word

# (72)素性抽出
#極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ
#素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラ\インとなるであろう
def make_feature(sentiment):
    y = []
    tfidf = TfidfVectorizer()

    x = np.array([line[3:] for line in sentiment])
    y = np.array([int(line[:2]) for line in sentiment])

    feature = tfidf.fit_transform(x)
    
    return feature, x, y, tfidf

    """
    feature = tfidf.fit_transform(sentiment)

    #print tfidf.get_feature_names()
    
    for line in sentiment:
        line = line.split()
        y.append(line[0])
        
    print '72 finish'
    return feature, y, tfidf
    """

def predict_probability(prediction):
    result = []
    
    for item in prediction:
        lst = []
        if item[0] > item[1]:
            lst.append('-1')
            lst.append('\t')
            lst.append(str(item))
            result.append(''.join(lst))
        else:
            lst.append('1')
            lst.append('\t')
            lst.append(str(item))
            result.append(''.join(lst))

    return result
    
def main():
    sentences = []
    test_data = ['She looks so happy.', 'This is an apple.', 'He looks sad. ']
    sentiment = exp70.read('sentiment.txt')
    """
    #stop_wordの検索
    for line in sentiment:
        line = line.split()
        for word in line:
            search_stop_word(word)

    print '71 finish' 
    """
    #(73)学習
    #72で抽出した素性を用いて、ロジスティック回帰モデルを学習せよ
    clf = LogisticRegression()
    feature_list, feature, label, tfidf = make_feature(sentiment)

    #Logistic regression
    clf.fit(feature_list, label)
    print '73 finish'

    #(74)予測
    #73で学習したロジスティック回帰モデルを用い、与えられた文の極性ラベル(正例なら"+1", 負例なら"-1")と、その予測確率を計算するプログラムを実装せよ.
    test = tfidf.transform(test_data)
    prediction = clf.predict_proba(test)

    print '74:predict_probability'
    probability_list = predict_probability(prediction)

    for item in probability_list:
        print item
        
    #(75)素性の重み
    #73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
    #feature_list = []
    weights =  clf.coef_
    names = tfidf.get_feature_names()

    #for weight in weights:
    #for (name, item) in zip(names, weight):
    feature_list = zip(names, weights[0])

    feature_list_sort = sorted(feature_list, key=lambda x:x[1], reverse=True)

    print '重みtop10'
    for item in feature_list_sort[:10]:
        print item

    print '重みworst10'
    for item in feature_list_sort[-10:]:
        print item
    
    #(76)ラベル付け
    #学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
    
    learning_data = tfidf.transform(feature)
    prediction_l = clf.predict_proba(learning_data)

    print '76:label'
    probability_list_l = predict_probability(prediction_l)
    
    for (item, probability) in zip(label, probability_list_l):
        print item, '\t', probability
    
        
if __name__ == '__main__':
    main()
    
        
