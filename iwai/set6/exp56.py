# !/usr/bin/python
# coding:UTF-8
# 6-(56):共参照解析
#Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import xml.etree.ElementTree as ET
import re
import exp50
import sys

#coreferenceのリストを作る
def make_coreference_list(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    coreferences = root.findall('document/coreference/coreference')

    return coreferences

def make_sentence_list(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    sentences = root.findall('document/sentences')

    sentence_list = []

    for sentence in sentences:
       for item in  sentence.findall('sentence'):
           sentence_list.append([word.text for word in item.findall('tokens/token/word')])
    
    return sentence_list



def main():
    fw = open('56.txt', 'w')
    sys.stdout = fw
    
    sentences = make_sentence_list('nlp_lined_rmHeader.txt.xml')
    coreference_list = make_coreference_list('nlp_lined_rmHeader.txt.xml')
    
    for coreference in coreference_list:
        mentions = coreference.findall('mention')
        for mention in mentions:
            if mention.attrib.get('representative') == 'true':
                rep = mention.find('text').text
            else:
                sentence_id = int(mention.find('sentence').text)-1
                start_id = int(mention.find('start').text)-1
                end_id = int(mention.find('end').text)-2

                sentences[sentence_id][start_id] = rep + '(' + sentences[sentence_id][start_id]
                sentences[sentence_id][end_id] = sentences[sentence_id][end_id] + ')'
                
    for sentence in sentences:
        print ' '.join(sentence)

    fw.close()
        
if __name__ == '__main__':
    main()
