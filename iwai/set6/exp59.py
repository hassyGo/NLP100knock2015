# !/usr/bin/python
# coding:UTF-8
# 6-(59):S式の解析
#Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import re
import sys
import exp50


#(が来た時、新しくリスト作ってappend続けて、)が来た時はそれまでappendしたリストをpopしてひとくくりにする
def make_parse_list(tree_split):
    
    tree_split = tree_split.split( )
    root = [[]]
    #test = []


    for item in tree_split:
        search1 = re.search('\w+', item)
        search2 = re.search('\,|\.|\?|\!', item)
        if item == '(':
            leaf = []
            root.append(leaf)
        if search1 or search2:
            leaf.append(item)
        if item == ')':
            root[-2].append(root.pop())

    return root

#(の後ろにスペースを入れて¥sでsplitできるようにする            
def add_space(parse_tree):
    parse_tree = re.sub('\(', '( ', parse_tree)
    parse_tree = re.sub('\)', ' )', parse_tree)

    return  parse_tree

#S式をとってくる
def s_list(document):
    lst = []
    parse = []
    
    for line in document:
        match = re.match('<parse>(.+)</parse>', line)

        if match:
            parse.append(match.group(1))
            lst.append(parse)
            parse = []
            
    return lst

#npタグのやつだけ取り出す
def make_np_list(lst):
    if isinstance(lst, list):
        np = []
        for item in lst:
            if isinstance(item, list):
                #print 'item:', item
                np += make_np_list(item)
            else:
                if item == 'NP':
                    np.append(lst)
                    #print 'NP:', np
                    
        return np


def extract_np(item):
    lst = []
    for i in item:
        if isinstance(i, list):
            #print 'iの要素:', i
            if isinstance(i[1], list):
                lst += extract_np(i)
            else:
                #print 'lst.append:', i[1] 
                lst.append(i[1])
    
    return lst
        
    
def main():
    fw = open('copy.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    parse_trees = s_list(document)

    for parse_tree in  parse_trees[1]:
        add_space_list = add_space(parse_tree)
        s = make_parse_list(add_space_list)
        np = make_np_list(s)

        for item in np:
            #print item
            np_word = extract_np(item)
            print ' '.join(np_word)
            
        #print np_word
        
    fw.close()
    
if __name__ == "__main__":
    main()


   
