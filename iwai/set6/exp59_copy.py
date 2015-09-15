# !/usr/bin/python
# coding:UTF-8
# 6-(59):S式の解析
#Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import re
import sys
import exp50


def print_line(test):
    keep = []
    pop = test.pop()
    if type(pop) == list:
        print 'popの要素: ', pop[-1]
        keep.append(pop[-1])
        
    return keep

def s_parser(tree_split):
    
    tree_split = tree_split.split( )
    root = [[]]
    test = []


    for item in tree_split:
        search1 = re.search('\w+', item)
        search2 = re.search('\,|\.|\?|\!', item)
        if item == '(':
            leaf = []
            root.append(leaf)
        if search1 or search2:
            leaf.append(item)
            if len(leaf) == 2:
                if 'NP' in leaf:
                    print 'left in NP: ', root[-1][1]
        if item == ')':
            root[-2].append(root.pop())
            if 'NP' in root[-1]:
                print 'left in NP(pattern B): ', root[-1]
                test = list(root[-1])
                cnt += 1
                print_line_lst = print_line(test)
                
        """
        if test:
            pop = test.pop()
            print 'pop: ', pop
            if type(pop) == list:
                print 'popの要素: ', pop[-1]
                keep.append(pop[-1])
        """     
    return root

            
def parse_tree_split(parse_tree):
    parse_tree = re.sub('\(', '( ', parse_tree)
    parse_tree = re.sub('\)', ' )', parse_tree)

    return  parse_tree
        
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
    
def main():
    fw = open('59.txt', 'w')
    sys.stdout = fw

    document = exp50.read('50.txt.xml')
    parse_trees = s_list(document)

    for parse_tree in  parse_trees[1]:
        tree_split = parse_tree_split(parse_tree)
        #print tree_split
        parser = s_parser(tree_split)
        print parser
        
    fw.close()
    
if __name__ == "__main__":
    main()


   
