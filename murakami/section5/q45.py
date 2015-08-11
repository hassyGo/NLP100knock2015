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




def getParticlesFromChunk(chunk,sentence):#chunkにかかる全ての助詞の文節の、助詞と文節のペアをタプルとするリストを返す
    #例えば「我輩は猫である」という文で、chunkが「猫である」だった場合、(は、我輩は)というタプルが返ってくる（この例は１個だけ）
    list = []
    for pindex in chunk.srcs: #chunkにかかっている文節すべてをチェック　pindexは対象となる文節の文中でのインデックス
        if sentence[pindex].isIncludePos("助詞"): #chunkに掛かっている文節が助詞を含んでいるか確認
            parIndex = sentence[pindex].getPosIndices("助詞")[-1] #一番右端にある助詞の位置を取得
            parBase = sentence[pindex].morphs[parIndex].base #取得した位置から、その形態素の原型を取得　「我輩は」から「は」を取得することになる
            parFull = sentence[pindex].getText() #こちらは対象となる文節の文字列を取得　「我輩は」そのものとなる。
            list.append((parBase,parFull)) #タプルにしてリストに追加
    return sorted(list) #0列目（助詞）に注目してそーとする。



if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    list = []
    
    for s in sentences:
        for c in s:
            if c.isIncludePos("動詞"): #動詞を含んでいる文節のみに着目
                verbIndex = c.getPosIndices("動詞")[0] #動詞が複数ある場合は、一番最初に出てくるものとする（最左）
                verbBase = c.morphs[verbIndex].base #その動詞の原型を形態素インスタンスから取得
                parList = getParticlesFromChunk(c,s) #着目している文節について、上で定義した関数を呼び、動詞の文節にかかっている助詞の文節からタプルとして情報を取得
                list.append((verbBase,parList)) #その情報をリストに順次追加

    ofs = open("q45_output.txt","w")

    for t in list: #結果を表示、保存
        string = "%s\t%s" % (t[0]," ".join(map(lambda n:n[0], t[1]))) #タプルの１個目を表示する　つまり、リストの要素の各１列目だけを表示することになる
        print string
        ofs.write(string.encode('utf-8')+"\n")

