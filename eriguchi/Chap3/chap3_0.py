#!/usr/bin/env python
# coding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json, urllib
import re

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
def ExtSenOfEnCate(data):
    p = re.compile(".*Category.*")
    sen_lst = data["text"].split("\n")
    lst = []
    for i in sen_lst:
        m = p.search(i)
        if m:
            print m.group()
            lst.append(m.group())
    return lst

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
def ExtCateNameOfEn(lst):
    p  = re.compile(":.*?\]")
    for i in lst:
        m = p.search(i)
        if m:
            print m.group().lstrip(":").rstrip("]")

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""
def SectStruct(data):
    p = re.compile("==.+==")
    sen_lst = data["text"].split("\n")
    for i in sen_lst:
        m = p.search(i)
        if m:
            moji  = m.group()
            count =  (moji.count("=")/2) -1
            print moji.replace("=", ""), count
            
"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
def ExtFileRef(data):
    p  = re.compile(u"\[\[ファイル.*?\||\[\[File.*?\|")
    p2 = re.compile(u"\[\[ファイル:|\[\[File:")
    sen_lst = data["text"].split("\n")
    for i in sen_lst:
        m = p.search(i)
        if m:
            moji = m.group()
            moji = p2.sub("", moji)
            print moji.replace("|", "")

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""
def ExtTemplate(data):
    temp_dic = {}
    
    p  = re.compile(u"\{\{基礎情報(.*\n)+?\}\}")
    p2 = re.compile(u".*?=")
    sen_lst = data["text"]
    m    = p.search(sen_lst)
    if m:
        moji = m.group()
        moji = re.sub(u"(\{\{)|(\n\}\})","", moji) # "{{", "}}"除去
        moji = moji.split("\n|")
        for i in moji[1:]:
            i = i.split(" = ")
            i[1] = RmMarkup(i[1])      # Remove MarkUp Emphasizing
            i[1] = RmInnerLink(i[1])   # Remove Markup Inner Link
            i[1] = RmOtherMarkup(i[1]) # Remove Other Markup
            temp_dic[i[0]] = i[1]
    return temp_dic
            
"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""
def RmMarkup(line):
    p = re.compile(u"\'\'[\']*(.+?)\'\'[\']*") # 弱い強調/ 強調/ 強い強調
    iterator = p.finditer(line)
    line2 = ""
    start = 0
    print "\n(3-6):"
    for i in iterator:
        line2 += line[start:i.start()] + i.group(1)
        start = i.end()
    if start <= len(line):
        line2 += line[start:]
        #print line2        
    return line2

"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""
def RmInnerLink(line):
    p  = re.compile(u"\[\[(.+?)\]\]") # 内部リンク
    p2 = re.compile(u"\||\#") 
    iterator = p.finditer(line)
    line2 = ""
    start = 0
    print "\n(3-7):"
    for i in iterator:
        line2 += line[start:i.start()] + p2.sub("", i.group(1))
        start = i.end()
    if start <= len(line):
        line2 += line[start:]
        #print line2        
    return line2

"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
def RmOtherMarkup(line):
    p  = re.compile(u"<(.+?)>|\}+") # <タグ>, 括弧あまり
    p2 = re.compile(u"\n\*+")         # 箇条書き, 
    p3 = re.compile(u"\||\[|\]")      # |, [, ] 1文字記号
    
    line = p.sub("", line)
    line = p2.sub("\n", line)
    line = p3.sub(" ", line)
    print "\n(3-8):"
    #print line
    return line

"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""
def GetFlagURL(temp_dic):    
    title = temp_dic[u"国旗画像"]
    title = title.replace(" ", "%20")
    
    URL = "http://en.wikipedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url&format=json&titles=File:" + title # Wikipedia API
    opener = urllib.urlopen(URL)
    data = opener.read()
    file_data = json.loads(data)
    # print(json.dumps(file_data, sort_keys=True, indent=4)) # 中身表示
    key_num = file_data["query"]["pages"].keys()[0]
    print file_data["query"]["pages"][key_num]["imageinfo"][0]["url"]

def main():
    f_path = './jawiki-country.json'
    f = open(f_path, 'r')
    line = f.readline()

    while line:
        data = json.loads(line)
        if data["title"] == u"イギリス":
            print data["text"] # Chap3-0
            break
        line = f.readline()

    print "\n(3-1):"
    cate_lst = ExtSenOfEnCate(data) # Chap3-1

    print "\n(3-2):"
    ExtCateNameOfEn(cate_lst)

    print "\n(3-3):"
    SectStruct(data)

    print "\n(3-4):"
    ExtFileRef(data)

    print "\n(3-5):"
    temp_dic = ExtTemplate(data)

    print "\n(3-9):"
    GetFlagURL(temp_dic)

if __name__ == "__main__":
    main()

