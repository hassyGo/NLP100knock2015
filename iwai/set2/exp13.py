# !/usr/bin/python
# coding:UTF-8
# 2-(13)

f1 = open("col1.txt", "r")
f2 = open("col2.txt", "r")
fw = open("all.txt", "w")

for line in f1:
    line1 = line.replace("\n", "\t")
    line2 = f2.readline()
    fw.write(line1 + line2)


f1.close()
f2.close()
fw.close()


#読み込むファイルの長さが違うときはどうするのか
#一応空白文字が出力されて、エラーになることはない
