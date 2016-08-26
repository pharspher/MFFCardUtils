#!/usr/bin/env python3

from utils import read_card_data


def list_cards():
    card_data = read_card_data()

    for card in card_data:
        print("Card " + str(card_data.index(card)))
        card.print_attributes()
        print("--------------------------------")
