#!/usr/bin/env python
#coding: utf-8

"""
    47. 機能動詞構文のマイニング
    動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
    
    「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
    述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
    述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
    述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
    例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文（949行目）から，以下の出力が得られるはずである．
    
    返事をする      と に は        及ばんさと 手紙に 主人は
    このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
    
    コーパス中で頻出する述語（サ変接続名詞+を+動詞）
    コーパス中で頻出する述語と助詞パターン
"""


from q40 import *
from q41 import *
from q42 import *

from q45 import *


if __name__ == "__main__":

    sentences = makeSentenceListFromXml("neko.xml")
    
    list = []
    
    for s in sentences[948:949]: #[948:949]が例
        for c in s:
            if c.isIncludePos("動詞"):
                verbIndex = c.getPosIndices("動詞")[0]
                verbBase = c.morphs[verbIndex].base
                for pindex in c.srcs:
                    parChunk = s[pindex]
                    if len(parChunk.morphs) == 2:
                        if parChunk.morphs[0].pos1 == u"サ変接続" and parChunk.morphs[1].pos == u"助詞" and parChunk.morphs[1].surface == u"を":
                            pred = parChunk.morphs[0].surface + parChunk.morphs[1].surface + verbBase
                
                            parList = getParticlesFromChunk(c,s)[:-1]
                            list.append((pred,parList))

    ofs = open("q47_output.txt","w")
    
    for t in list:
        string = "%s\t%s\t%s" % (t[0]," ".join(map(lambda n:n[0], t[1])) ," ".join(map(lambda n:n[1], t[1])))
        print string
        ofs.write(string.encode('utf-8')+"\n")