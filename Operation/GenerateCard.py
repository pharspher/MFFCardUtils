#!/usr/bin/env python3

from Card import Card
from IOUtils import read_card_data, save_card_data
from Utils import print_card


def print_options():
    print()
    hint = ""
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        hint = hint + str(index) + ". " + attribute + "\n"
    print(hint)


def generate_card():
    done = False

    card_data = read_card_data()

    card = Card(len(card_data))

    while not done:
        print_options()
        input_attr = input("attribute: ")

        if len(input_attr.strip()) == 0:
            done = True
            continue

        input_value = input("value: ")
        card.attributes[Card.attribute_names[int(input_attr)]] = input_value

    if len(card.attributes.keys()) == 0:
        print("no attribute set, cancel")

    else:
        print_card(card)
        card_data.append(card)
        save_card_data(card_data)
