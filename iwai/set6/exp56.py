# !/usr/bin/python
# coding:UTF-8
# 6-(56):共参照解析
#Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import re
import sys

if __name__ == "__main__":
    fw = open('56.txt', 'w')
    sys.stdout = fw

    sentence = []
    flag = 0
    document = exp50.read('nlp.txt.xml')
    
        
    fw.close()
