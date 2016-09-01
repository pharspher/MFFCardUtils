#!/usr/bin/env python3

from __future__ import print_function
from Card import Card
from Operation.Utils import *
from Utils import *


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
                resolved_attribute_name = resolve_attribute_name(attribute[0].strip(), attribute[1].strip(), False)
                if resolved_attribute_name == None:
                    print_warn("invalid card data")
                card_list[-1].attributes[resolved_attribute_name] = attribute[1].strip()

    return card_list


def save_card_data(card_data, file_name="cards_data"):
    with open(file_name, "w") as fd:
        for card in card_data:
            print("#card", file=fd)

            for attribute in card.attributes.keys():
                print(attribute + ": " + card.attributes[attribute], file=fd)

            print("\n", file=fd)


def read_exclusive_group():
    with open("exclusive_data", "r") as fd:
        lines = fd.readlines()
    
    groups = []
    
    for raw_line in lines:
        line = raw_line.strip()
        split_line = line.split(" ")
        group = []
        for i in range(len(split_line)):
            group.append(int(split_line[i]))
        groups.append(group)
        
    return groups