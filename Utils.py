#!/usr/bin/env python3

from Card import Card
from itertools import combinations

def read_card_data(dataName = "cards_data"):
    with open(dataName) as file:
        lines = file.readlines()
        
    cardList = []
    
    cardCount = 0
    
    for unstripLine in lines:
        line = unstripLine.strip()
        
        if (line == "#card"):
            card = Card(cardCount)
            cardList.append(card)
            cardCount = cardCount + 1
            
        else:
            attribute = line.split(":")
            
            if len(attribute) != 2:
                continue
            else:
                cardList[-1].attributes[attribute[0].strip()] = attribute[1].strip()
                
    return cardList

def save_card_data(cardData, dataName = "cards_data"):
    with open(dataName, "w") as f:
        for card in cardData:
            print("#card", file = f)
            for attribute in card.attributes.keys():
                print(attribute + ": " + card.attributes[attribute], file = f)
            print("\n", file = f)
            
        

def generate_attribute_vector(card):
    attributes = card.attributes