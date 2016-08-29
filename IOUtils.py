#!/usr/bin/env python3

from __future__ import print_function
from Card import Card


def read_card_data(file_name="cards_data"):
    with open(file_name) as fd:
        lines = fd.readlines()

    card_list = []

    card_count = 0

    for raw_line in lines:
        line = raw_line.strip()

        if line == "#card":
            card = Card(card_count)
            card_list.append(card)
            card_count += 1

        else:
            attribute = line.split(":")

            if len(attribute) != 2:
                continue
            else:
                card_list[-1].attributes[attribute[0].strip()] = attribute[1].strip()

    return card_list


def save_card_data(card_data, file_name="cards_data"):
    with open(file_name, "w") as fd:
        for card in card_data:
            print("#card", file=fd)

            for attribute in card.attributes.keys():
                print(attribute + ": " + card.attributes[attribute], file=fd)

            print("\n", file=fd)
