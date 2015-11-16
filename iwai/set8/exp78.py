# !usr/bin/python
# coding:UTF-8
#(78)5分割交差検定
#76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ

from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import numpy as np 
import sys
import random
import string
import nltk
import exp70
import exp71_exp76 as exp76

def cross_validation(sentiment):
    acc = []
    pre = []
    rec = []
    f = []
    
    #clf = LogisticRegression()
    #tfidf = TfidfVectorizer() 

    x = np.array([line[3:] for line in sentiment]) 
    y = np.array([int(line[:2]) for line in sentiment])

    #feature_list, feature, label, tfidf = exp76.make_feature(sentiment) 
    
    cv = KFold(n=len(sentiment), n_folds=5)

    for train, test in cv:
        clf = LogisticRegression()
        tfidf = TfidfVectorizer() 

        X_train, y_train = x[train], y[train]
        X_test, y_test = x[test], y[test]

        #ロジスティック回帰による学習
        feature = tfidf.fit_transform(X_train)   
        clf.fit(feature, y_train)

        #極性分類の正解率
        test = tfidf.transform(X_test)
        y_pred = clf.predict(test)
        accuracy = accuracy_score(y_test, y_pred)
        acc.append(accuracy)

        #適合率, 再現率、f値
        precision, recall, f_score, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')
        pre.append(precision)
        rec.append(recall)
        f.append(f_score)
        
    #return map(np.mean, [acc, pre, rec, f])
    return [np.mean(i) for i in [acc, pre, rec, f]]   
        
def main():
    sentiment = exp70.read('sentiment.txt')

    result = cross_validation(sentiment)
    print result

    
if __name__ == '__main__':
    main()
    
        
