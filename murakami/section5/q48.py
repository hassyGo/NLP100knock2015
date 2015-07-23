#!/usr/bin/env python
#coding: utf-8

"""
    48. 名詞から根へのパスの抽出
    文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．
    
    各文節は（表層形の）形態素列で表現する
    パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
    「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
    
    吾輩は -> 見た
    ここで -> 始めて -> 人間という -> ものを -> 見た
    人間という -> ものを -> 見た
    ものを -> 見た
"""


from q40 import *
from q41 import *
from q42 import *

#あるchunkからルートに至るまでの係り受け連鎖をchunkリストで取得
def getListToRoot(chunk,sentence):
    currentChunk = chunk
    list = [currentChunk]
    while currentChunk.dst != -1:
        currentChunk = sentence[currentChunk.dst]
        list.append(currentChunk)
    return list

#stringBeginとstringEndはそれぞれリストの先頭と末尾の名詞句を置き換える文字列を設定する(空の時は置き換えない)
#input [a,b,c,d],"X","Y"  output X -> b -> c -> Y
def getArrowString(chunkList,stringBegin,stringEnd):
    string = ""
    for i in range(len(chunkList)):
        if i == 0:
            string += chunkList[i].getNPReplaceText(stringBegin)
        elif i == len(chunkList)-1:
            string += chunkList[i].getNPReplaceText(stringEnd)
        else:
            string += chunkList[i].getText()
        if i != len(chunkList)-1:
            string += " -> "
    return string


if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    for s in sentences[7:8]:
        for c in s:
            if c.isIncludePos("名詞"):
                list = getListToRoot(c,s)
                print getArrowString(list,"","")

