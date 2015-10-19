#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import exp
import random

def convertEnjuData(enjuFile, labelStr):
    f = open(enjuFile);
    sample = ""
    isBeginning = True

    for line in f:
        line = line.rstrip()

        if line == "":
            print sample
            isBeginning = True
            continue

        if isBeginning:
            sample = labelStr
            isBeginning = False

        fields = line.split()

        if fields[2] != "tok":
            continue

        sample += " "+fields[6].split("\"")[1]

def isStopWord(stopList, word):
    return stopList.has_key(word)

class Instance:
    def __init__(self, label):
        self.label = label
        self.features = []

class LogisticRegression:
    def __init__(self, featureNum):
        self.weights = [0.0]*featureNum
        self.bias = 0.0

    def logisticFunc(self, val):
        return 1.0/(1.0+exp(-val))

    def calcScore(self, instance):
        score = 0.0
        for feature in instance.features:
            score += self.weights[feature]
        return self.logisticFunc(score)
    
    def update(self, instance, learningRate):
        score = self.calcScore(instance)
        delta = score-instance.label
        self.bias -= learningRate*delta
        for feature in instance.features:
            self.weights[feature] -= learningRate*delta

    def getLabel(self, instance):
        if self.calcScore(instance) >= 0.5:
            return 1
        else:
            return 0

    def classify(self, instance):
        return instance.label == self.getLabel(instance)

if __name__ == '__main__':
    #convertEnjuData("rt-polaritydata/rt-polarity.neg.enju-so", "-1")
    #convertEnjuData("rt-polaritydata/rt-polarity.pos.enju-so", "+1")
    ## % cat rt-polaritydata.pos.base rt-polaritydata.neg.base | sort -R > sentiment.txt
    ## % grep "^+1 " sentiment.txt | wc -l
    ## % grep "^-1 " sentiment.txt | wc -l

    ##load a stop word list
    f = open("./stopwords")
    stopList = {}
    for stopWord in f.read().rstrip().split(","):
        stopList[stopWord] = 1
    f.close()

    ##check whether some words are included in the list and others are not included in it
    #print isStopWord(stopList, "a") # True
    #print isStopWord(stopList, "-COMMA-") # True
    #print isStopWord(stopList, "great") # False
    #print isStopWord(stopList, "dull") # False

    ##load the training data
    f = open("./sentiment.txt")
    trainingData = []
    unigram = {}
    featureIndex = 0
    for line in f:
        fields = line.rstrip().split()
        if int(fields[0]) == 1:
            instance = Instance(1)
        else:
            instance = Instance(0)

        ##assign unigram features for each training data
        for i in range(1, len(fields)):
            if isStopWord(stopList, fields[i]):
                continue
            if not unigram.has_key(fields[i]):
                unigram[fields[i]] = featureIndex
                featureIndex += 1
            instance.features.append(unigram[fields[i]])
        trainingData.append(instance)
    f.close()

    ##train a logistic regression model
    classifier = LogisticRegression(featureIndex)
    epochNum = 50
    learningRate = 1.0
    for i in range(epochNum):
        random.shuffle(trainingData)

        for instance in trainingData:
            classifier.update(instance, learningRate)

        #classify the training data
        numCorrect = 0.0
        for instance in trainingData:
            if classifier.classify(instance):
                numCorrect += 1
        print "Epoch", i+1, ":", 100*numCorrect/len(trainingData), "%"
        learningRate *= 0.999
