#!/usr/bin/env python3

from .Operation import Operation

from Card import Card
from Utils import read_card_data
from Utils import save_card_data

class GenerateCard(Operation):
    def run(self):
        done = False
        
        cardData = read_card_data()
        
        card = Card(len(cardData))
        
        while done == False:
            self.printOptions()
            inputAttr = input("attribute: ")
            
            if len(inputAttr.strip()) == 0:
                done = True
                continue
            
            inputValue = input("value: ")
            card.attributes[Card.attributeIndex[int(inputAttr)]] = inputValue
            
        if len(card.attributes.keys()) == 0:
            print("no attribute set, cancel")
            
        else:
            card.print()
            cardData.append(card)
            save_card_data(cardData)
            
    def printOptions(self):
        print()
        hint = ""
        for attribute in Card.attributeIndex:
            index = Card.attributeIndex.index(attribute)
            hint = hint + str(index) + ". " + attribute + "\n"
        print(hint)