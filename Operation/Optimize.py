#!/usr/bin/env python3

from .Operation import Operation

from itertools import combinations
from Utils import read_card_data
from Card import Card

class Optimize(Operation):
    def __init__(self, pickCount):
        self.pickCount = pickCount
    
    def run(self):
        cards = read_card_data()
        
        vectors = []
        for card in cards: vectors.append(card.toVector())
        
        cardSetList = []
        
        indexCombinations = combinations(range(len(vectors)), self.pickCount)
        for indexCombination in indexCombinations:
            cardSet = []
            for index in indexCombination:
                cardSet.append(cards[index])
                
            cardSetList.append(cardSet)
            
        print("number of card combination: " + str(len(cardSetList)))
        
        print("============================")
        
        for cardSet in cardSetList:
            vector = self.sumVectors(cardSet)
            cooldownIndex = Card.attributeIndex.index("cooldown")
            allAttackIndex = Card.attributeIndex.index("all_attack")
            ignoreIndex = Card.attributeIndex.index("defense_ignore")
            
            if vector[cooldownIndex] < 25:
                continue
            
            if vector[allAttackIndex] < 20:
                continue
            
            if vector[ignoreIndex] < 5:
                continue    
            
            cardList = ""
            for card in cardSet:
                cardList = cardList + str(card.index) + ", "
            print("Cards: [" + cardList + "]")
            print("----------------------------")
            self.printAttribute(vector)
            print("============================")
    
    def vectorSet(self, cardSet):
        vectorSet = []
        for card in cardSet:
            vectorSet.append(card.toVector())
            
        return vectorSet
    
    def sumVectors(self, cardSet):
        vectors = self.vectorSet(cardSet)
        
        sumVector = []
        
        for dimen in range(len(Card.attributeIndex)):
            sum = 0
            for vector in vectors:
                sum = sum + vector[dimen]
            sumVector.append(sum)
            
        return sumVector
    
    def printVector(self, vector):
        str = "["
        for dimenValue in vector:
            str = str + "{0:6.2f}".format(dimenValue) + ", "
        str = str + "]"
        print(str)
        
    def printAttribute(self, vector):
        for attribute in Card.attributeIndex:
            index = Card.attributeIndex.index(attribute)
            if vector[index] == 0:
                continue
            print("{0:20}: {1:6.2f}".format(attribute, vector[index]))
                
        
        