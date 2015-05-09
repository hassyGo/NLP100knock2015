# coding: UTF-8

import random


#http://docs.python.jp/2/library/string.html

def getInverseString(s):
    #a = ""
    #for i in range(len(s)):
    #   a += s[len(s)-1-i]
    #return a
    return s[::-1]

def getOddString(s):
    #a = ""
    #for i in range(len(s)/2):
    #   a += s[i*2+1]
    #return a
    return s[::2]

def addAlternateString(a,b):
    s = ""
    #zipを使う
    for i in range(len(a)):
        s += a[i]
        s += b[i]
    return s

def getListOfLengths(s):
    nl = []
    sl = s.split()
    for w in sl:
        w = w.split(",")[0]
        w = w.split(".")[0]
        nl.append(len(w))
    return nl

def getChemicalElementMap(s):
    dic = {}
    firstList = [1,5,6,7,8,9,15,16,19]
    words = s.split()

#dic = {}

    for i in range(len(words)):
        index = i+1
        if index in firstList:
            dic[words[i][0:1]] = index
        else:
            dic[words[i][0:2]] = index
    
    return dic

def getNGram(s,n):
    l = []
    if isinstance(s,list):
        for i in range(len(s)-n+1):
            word = ""
            for j in range(n):
                word += s[i+j]
                if j!=n-1:
                    word += " "
            l.append(word)
    else:
        words = s.split()
        for w in words:
            for i in range(len(w)-n+1):
                word = ""
                for j in range(n):
                    word += w[i+j]
                l.append(word)
    return l

def getTemplateString(x,y,z):
    #return "%d時の%sは%.1f",(x,y,z)
    return "" + str(x) + "時の" + str(y) + "は" + str(z)

def encoder(s):
    a = ""
    for w in s:
        if w != None:
            if w.islower():
                a += chr(219-ord(w))
            else:
                a += w
    return a

def getCenterRandomString(s):
    a = ""
    if len(s) <= 4:
        a = s
    else:
        #l = [s[i] for i in range(1,len(s)-1)]
        l = s[1:-1]
        for i in range(1,len(s)-1):
            l.append(s[i])
        random.shuffle(l)
        a += s[0]
        for w in l:
            a += w
        a += s[-1]
    return a


string = "stressed"
print "00:", string, getInverseString(string)

string = u"パタトクカシーー"
print "01:", string, getOddString(string)

str1 = u"パトカー"
str2 = u"タクシー"
print "02:", str1, str2, addAlternateString(str1,str2)

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print "03:", getListOfLengths(string)
        
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print "04:", getChemicalElementMap(string)

string = "I am an NLPer"
strs = string.split()
print "05:",getNGram(string,2), getNGram(strs,2)


str1 = "paraparaparadise"
str2 = "paragraph"
X = set(getNGram(str1,2))
Y = set(getNGram(str2,2))
print "06:", "X", X, "Y", Y
print "X+Y", X|Y
print "X*Y", X&Y
print "X-Y", X-Y
print "'se' in X:", "se" in X, "   'se' in Y:", "se" in Y



print "07:", getTemplateString(12,"気温",22.4)


string = "encode ENCODE EnCoDe"
print "08:", string, "/", encoder(string)

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
strs = string.split()
string = ""
for i in range(len(strs)):
    string += getCenterRandomString(strs[i])
    if i!= len(strs)-1:
        string += " "
print "09:", string
