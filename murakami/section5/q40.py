#!/usr/bin/env python
#coding: utf-8

"""
    40. 係り受け解析結果の読み込み（形態素）
    形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""


import xml.etree.ElementTree as ET #xmlファイルから自動的に木構造を生成するライブラリ
import itertools #その木構造のイテレーションを制御するためのライブラリ


class Morph: #形態素のクラス
    def __init__(self,feature,text): #コンストラクタ (インスタンスが生成されるときに自動的に呼ばれる関数) 引数は、feature:形態素の特徴を表すカンマ区切りの文字列 text:形態素の表層形文字列
        list = feature.split(",") #それぞれ適切に代入
        self.surface = text
        self.base = list[6]
        self.pos = list[0]
        self.pos1 = list[1]

    def getString(self): #形態素のインスタンスを表示するために、適切な形で情報を含んだ文字列を返す関数
        return "(surface=%s,base=%s,pos=%s,pos1=%s)" % (self.surface,self.base,self.pos,self.pos1)


#インスタンスとは、クラス（設計図のようなもの）から生成された実体（実際にメモリを消費する）
#m = Morph("名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ","吾輩")　のように記述すると、クラスMorphからインスタンスmがつくられる。
#n = Morph("名詞,一般,*,*,*,*,名前,ナマエ,ナマエ","名前")　としたときに、mとnは同じクラスMorphから生成されているが、全く別のインスタンスである。
#例えば、m.surface は「我輩」であるが、n.surface は「名前」となっている。


def printMorphList(list): #python3ではないので、普通にリストをprintすると文字化けしてしまう。そこで、適切にリストを表示してくれるこの関数を生成
    print "[" + ",".join([m.getString() for m in list]) + "]" #こうしておくと毎度for文を書く必要がなくなる


def readXml(filename): #filenameを文字列で渡してあげると、自動的にxmlデータから木構造を作ってくれる。最終的にもどってくるのはrootノードの情報。これをもとに木を巡回する。
    with open(filename) as f:
        it = itertools.chain('<root>', f, '</root>')#もしルートタグがない場合はつける
        root = ET.fromstringlist(it)
    return root


if __name__ == "__main__": #メイン関数のようなもの　ここからプログラムが始まる　基本的に必要な部品はすでに上で作っているので、それを適切な順番で呼ぶだけ。
    root = readXml("neko.xml") #neko.xmlから木構造を作る

    #以下の処理はq41でやるように関数にしてしまってもいいが、この処理自体は他で使いまわさないので、ここで直接ベタ書きにした。
    sentences = []
    for sIte in root: #つくった木構造からforでイテレーションを回しつつ、深さ優先で木を調べていく。sIteは各文を指す。
        tmpSentence = []
        for cIte in sIte: #cIteは、ある文中の各チャンクを指す。
            for mIte in cIte: #mIteは、あるチャンク中の各形態素を指す
                m = Morph(mIte.get("feature"),mIte.text) #ここでmIteが差している形態素情報から、形態素インスタンスmを生成する。
                tmpSentence.append(m) #そのmをtmpSentenceに追加していく
    
        sentences.append(list(tmpSentence)) #各文が終了するたびに、sentencesに、tmpSentence(形態素列)を追加していく。

    printMorphList(sentences[2]) #3文目の結果を表示する

