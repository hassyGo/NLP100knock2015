#!/usr/bin/env python
#coding: utf-8

"""
    81. 複合語からなる国名への対処
    英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．
    
    インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
"""

def country_connect(str,countryList):
    for country in countryList:
        replaceCountry = "_".join(country.split())
        str = str.replace(country,replaceCountry)
    return str

if __name__ == "__main__":
    f = open("country/countries.txt")
    countryList = [m.rstrip() for m in f.readlines() if m != ""]
    f.close()
    
    fo = open("enwiki_country_connected.txt","w")
    f = open("enwiki_formatted.txt")
    line = f.readline()

    while line:
        fo.write(country_connect(line.rstrip(),countryList)+"\n")
        line = f.readline()