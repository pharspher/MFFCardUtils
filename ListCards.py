#!/usr/bin/env python3

from Operation import Operation
from Utils import read_card_data

class ListCards(Operation):
    def run(self):
        cardData = read_card_data()
        
        for card in cardData:
            print("Card " + str(cardData.index(card)) + ": " + str(card.toVector()))
            card.print()
            print("\n")