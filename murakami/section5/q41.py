#!/usr/bin/env python
#coding: utf-8

"""
    41. 係り受け解析結果の読み込み（文節・係り受け）
    40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

#import q40
from q40 import * #このように記述しておくと、q40.pyの中で宣言した関数が、何事もなかったようにこっちのコードでも使えるようになる。
import xml.etree.ElementTree as ET
import itertools
import re


class Chunk:
    def __init__(self,id,link,linked): #チャンクのコンストラクタ（インスタンス生成時に自動的に呼ばれる)
        self.morphs = [] #形態素列 list
        self.dst = int(link) #かかり先ID int
        self.id = int(id) #自分のID int
        self.srcs = linked #かかり元ID list

    def pushMorph(self,m): #チャンクに形態素インスタンスを追加していく関数（メソッド）
        self.morphs.append(m)
    
    
    def getText(self): #文節の文字列を返す。こうしておけば毎度for文を回す必要がなくなる。
        return "".join([m.surface for m in self.morphs if m.pos != u"記号"])
    
    #文節の名詞句を置き換えた文字列を返す(stringが空の時は置き換えない)　q48やq49で使う。
    def getNPReplaceText(self,string):
        if string == "":return self.getText() #入力が空のときは置き換えなどせずに普通に文字列を返す（上のgetTextを呼ぶだけ）
        s = ""
        for m in self.morphs:
            if m.pos == u"記号":continue
            if m.pos == u"名詞":
                s += string
            else:
                s += m.surface
    
        s = re.sub(u'XX+','X',s) #"XX"  や "XXX"などの表示を"X"に直している
        return s
    

    #文節の文字列とかかり先をstringで返す チャンクの情報を適切に表す文字列を取得するのに使う。
    def getString(self):
        return "(string=%s,dst=%d)" % (self.getText() ,self.dst)
    
    #文節の情報すべてをstringで返す チャンクの情報を適切に表す文字列を取得するのに使う。
    def getInfoString(self):
        linkedString = ",".join([str(i) for i in self.srcs])
        return "(id=%d,string=%s,dst=%d,srcs=" % (self.id ,self.getText() ,self.dst) + linkedString + ")"

    #文節の中にPOSを含むものがあるならTrue 後ろの方の問題で、文節中に名詞が含まれたら〜、などのときに c.isIncludePos("名詞")とすると、チャンクcが名詞を含んでいるかどうかが一発でわかる。
    def isIncludePos(self,pos):
        return pos in [m.pos.encode('utf-8') for m in self.morphs]

    #文節の中のPOSと一致するindexのリストを返す　例えば、チャンクcの中の先頭から３つ目と５つ目に名詞がある場合、c.getPosIndices("名詞")は　[2,4]　と同じ意味になる。
    def getPosIndices(self,pos):
        return [index for index in range(len(self.morphs)) if self.morphs[index].pos.encode('utf-8') == pos]

    #文節の中のPOS1と一致するindexのリストを返す
    def getPos1Indices(self,pos1):
        return [index for index in range(len(self.morphs)) if self.morphs[index].pos1.encode('utf-8') == pos1]


def printChunkList(list): #チャンク列を適切に表現するための関数 ふつうにやるとリストが文字化けしてしまうため。
    print "[" + ",".join([c.getString() for c in list]) + "]"
#print "[" + ",".join([c.getInfoString() for c in list]) + "]"


def makeSentenceListFromXml(filename): #毎回xmlからチャンク列を生成するのは面倒なので、この関数で一発でできるようにここで用意しておく
    #入力ではファイル名を受け取り、最終的な出力としては、
    #sentences
    #   |---sentence
    #   |---sentence
    #   |     ...
    #   |---sentence (chunkのリスト）
    #         |---chunk
    #         |---chunk
    #              ...
    #         |---chunk
    #のような構造（chunkリストのリスト）をもつsentencesを返す
    
    root = readXml(filename) #q40でつくった関数を使い回す　これでxmlファイルから木構造データのrootが返ってくる
    sentences = []
    for sIte in root:
        tmpSentence = []
        for cIte in sIte: #cIteは各文sIteの各チャンクを指す　cIte.get("id")で、「id」タグの値が取得できる
            linked = [int(m.get("id")) for m in sIte if m.get("link") == cIte.get("id")] #ある文中sIteにおけるチャンクの中で、今注目しているチャンクcIteとlinkが一致しているもの（cIteを指しているチャンク）のリストを取得する。つまりlinkedは文節cIteにかかっている文節のidのリスト
            c = Chunk(cIte.get("id"),cIte.get("link"),linked) #得られた情報をもとに、チャンクインスタンスcを生成（コンストラクタを呼ぶ）
            for mIte in cIte:
                m = Morph(mIte.get("feature"),mIte.text)
                c.pushMorph(m) #q40の時と同様に形態素列をつぎつぎに追加していく
            tmpSentence.append(c)
        sentences.append(list(tmpSentence))
    return sentences

if __name__ == "__main__": #ここまでで必要な部品は全部作ったので、あとはそれを適切な順で呼ぶだけ。今回はなんと２行しかない。
    sentences = makeSentenceListFromXml("neko.xml")
    
    printChunkList(sentences[7]) #8文目の結果を表示