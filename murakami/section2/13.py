# -*- coding: utf-8 -*-

#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ


import string

if __name__ == "__main__":
    
    lines = []
    for i in range(2):
        f = open("col%d.txt" % (i+1))
        lines.append(f.readlines())
        f.close()

    f = open("merge.txt","w")
    for (line1,line2) in zip(lines[0],lines[1]):
        f.write(line1.rstrip() + "\t" + line2.rstrip() + "\n")

#コマンドでやるなら
# paste col1.txt col2.txt 