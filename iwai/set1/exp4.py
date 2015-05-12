# !/usr/bin/python
# coding:UTF-8
# 1-(4)


str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = str.split()
print s

cnt = 0
#sub = []

d = {}

for i in range(0,20):
    cnt += 1
    if cnt == 1 or cnt == 5 or cnt == 6 or cnt == 7 or cnt == 8 or cnt == 9 or cnt == 15 or cnt == 16 or cnt == 19:
        d.update({s[i][0]: i+1})
    else:
        d.update({s[i][:2]: i+1})

#d = {1: s[0]}
print sorted(d.items(), key=lambda x:x[1])

#辞書は整列している必要はない

#enumerate()
#for i,j in enumerate(lst)
#i:要素の番号
#j:要素の中身
