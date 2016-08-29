#!/usr/bin/env python3

from IOUtils import read_card_data
from Utils import print_card


def list_cards():
    card_data = read_card_data()

    for card in card_data:
        print("Card " + str(card_data.index(card)))

        print_card(card)
        print("--------------------------------")
