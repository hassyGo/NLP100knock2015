#!/usr/bin/env python
#coding: utf-8

"""
    71. ストップワード
    英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""


def getStopWordList():
    return ["a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your","(",")",".",",","\"",":",";","?","!","'","-","--"]

def isIncludeStopword(word):
    stopwordlist = getStopWordList()
    return word in stopwordlist

if __name__ == "__main__":
    print isIncludeStopword("a"),isIncludeStopword("murakami"),isIncludeStopword("the")
