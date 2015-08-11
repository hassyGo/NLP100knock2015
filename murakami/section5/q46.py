#!/usr/bin/env python
#coding: utf-8

"""
    46. 動詞の格フレーム情報の抽出
    45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
    
    項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
    述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
    「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
    
    始める  で      ここで
    見る    は を   吾輩は ものを
"""


from q40 import *
from q41 import *
from q42 import *


from q45 import *


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

    ofs = open("q46_output.txt","w")

    #ここまでq45と全く一緒
    
    for t in list:
        string = "%s\t%s\t%s" % (t[0]," ".join(map(lambda n:n[0], t[1])) ," ".join(map(lambda n:n[1], t[1]))) #表示する際に、１列目だけでなく２列目も出力するようにするだけ。
        print string
        ofs.write(string.encode('utf-8')+"\n")