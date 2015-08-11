#!/usr/bin/env python
#coding: utf-8

"""
    49. 名詞間の係り受けパスの抽出
    文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
    
    問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
    文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
    また，係り受けパスの形状は，以下の2通りが考えられる．
    
    文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
    上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
    例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
    
    Xは | Yで -> 始めて -> 人間という -> ものを | 見た
    Xは | Yという -> ものを | 見た
    Xは | Yを | 見た
    Xで -> 始めて -> Y
    Xで -> 始めて -> 人間という -> Y
    Xという -> Y
"""


from q40 import *
from q41 import *
from q42 import *

from q48 import *



def getArrowStringXYK(chunkList1,chunkList2,chunkK): #kを含む場合の適切な文字列を返す関数
    return getArrowString(chunkList1,"X","") + " | " + getArrowString(chunkList2,"Y","") + " | " + chunkK.getText()

def getChunkKFromTwoIndice(indice1,indice2): #kを含む場合に、二つのチャンクからkの位置を求める関数
    set1 = set(indice1)
    set2 = set(indice2)
    candidateK = set1 & set2
    for index in indice1:
        if index in candidateK: return index
    return -1


if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    
    for s in sentences[7:8]:#[7:8]で例
        for i in range(len(s)):
            if s[i].isIncludePos("名詞") == False:continue
            for j in range(i+1,len(s)):
                if s[j].isIncludePos("名詞") == False:continue
                ilist = getListToRoot(s[i],s) #chunkのリスト
                jlist = getListToRoot(s[j],s)
                iIndice = [m.id for m in ilist] #chunk.idのリスト
                jIndice = [m.id for m in jlist]
            
                if j in iIndice: #一つ目の条件にマッチ
                    index = iIndice.index(j)
                    print getArrowString(ilist[0:index+1],"X","Y")

                else: #二つ目の条件にマッチ
                    k_id = getChunkKFromTwoIndice(iIndice,jIndice)
                    indexi = iIndice.index(k_id) #それぞれchunkKが何番目にあるか調べる
                    indexj = jIndice.index(k_id)
                    print getArrowStringXYK(ilist[0:indexi],jlist[0:indexj],ilist[indexi]) #結果を表示
