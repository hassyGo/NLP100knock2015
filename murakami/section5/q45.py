#!/usr/bin/env python
#coding: utf-8

"""
    45. 動詞の格パターンの抽出
    今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．
    
    動詞を含む文節において，最左の動詞の基本形を述語とする
    述語に係る助詞を格とする
    述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
    「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
    
    始める  で
    見る    は を
    このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
    
    コーパス中で頻出する述語と格パターンの組み合わせ
    「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""


from q40 import *
from q41 import *
from q42 import *


#chunkにかかる全ての助詞の文節の、助詞と文節のペアをタプルとするリストを返す
def getParticlesFromChunk(chunk,sentence):
    list = []
    for pindex in chunk.srcs:
        if sentence[pindex].isIncludePos("助詞"):
            parIndex = sentence[pindex].getPosIndices("助詞")[-1]
            parBase = sentence[pindex].morphs[parIndex].base
            parFull = sentence[pindex].getText()
            list.append((parBase,parFull))
    return sorted(list)



if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    list = []
    
    for s in sentences:
        for c in s:
            if c.isIncludePos("動詞"):
                verbIndex = c.getPosIndices("動詞")[0]
                verbBase = c.morphs[verbIndex].base
                parList = getParticlesFromChunk(c,s)
                list.append((verbBase,parList))

    ofs = open("q45_output.txt","w")

    for t in list:
        string = "%s\t%s" % (t[0]," ".join(map(lambda n:n[0], t[1])))
        print string
        ofs.write(string.encode('utf-8')+"\n")

