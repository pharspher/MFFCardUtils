#!/usr/bin/env python3

from Card import Card
from IOUtils import read_card_data, save_card_data
from Operation.Utils import *
from Utils import *


def print_options():
    print()
    seperate()
    options = ""
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        options += (str(index) + ". " + attribute + "\n")
    print(hint(options))


def create_new_card():
    done = False

    card_data = read_card_data()
    card = Card(len(card_data))

    while not done:
        print_options()
        input_line = input(prompt("enter \"attr value\": "))
        
        if len(input_line.strip()) == 0:
            done = True
            continue
        
        split_line = input_line.split(" ")
        
        length = len(split_line)
        
        if length == 0 or length % 2 != 0:
            done = True
            continue
        
        for i in range(0, len(split_line) - 1, 2):
            attr = split_line[i].strip()
            value = split_line[i + 1].strip()
        
            resolved_attribute_name = resolve_attribute_name(attr, value)
            if resolved_attribute_name == None:
                continue
            card.attributes[resolved_attribute_name] = value

    if len(card.attributes.keys()) == 0:
        print_warn("no attribute set, cancel")
        return None

    else:
        print_card(card)
        return card


def generate_card():
    card_data = read_card_data()
    card = create_new_card()
    
    if card != None:
        card_data.append(card)
        save_card_data(card_data)
