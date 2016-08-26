#!/usr/bin/env python3

from .Operation import Operation

from Utils import read_card_data
from Utils import save_card_data

class RemoveCard(Operation):
    def run(self):
        cardData = read_card_data()
        
        cardIndex = int(input("Card index: "))
        
        card = cardData[cardIndex]
        print("Card-" + str(card.index))
        card.print()
        
        answer = input("remove[y, n]? ")
        
        if answer == "y":
            del cardData[cardIndex]
            save_card_data(cardData)