#!/usr/bin/env python3

from Card import Card
from IOUtils import read_card_data, save_card_data
from Utils import *


def print_options():
    print()
    seperate()
    options = ""
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        options += (str(index) + ". " + attribute + "\n")
    print(hint(options))


def find_attribute(input_attribute, input_value):
    find_result = []
    
    for attribute_name in Card.attribute_names:
        if attribute_name.startswith(input_attribute):
            find_result.append(attribute_name)
    
    if len(find_result) == 1:
        return find_result[0]
        
    print_warn("ambiguous: " + input_attribute + " " + str(input_value))
        
    option_string = ""    
    for i in range(len(find_result)):
        option_string += (str(i + 1) + ". " + find_result[i] + ", ")
    
    print(hint(option_string))
    
    done = False
    
    while not done:
        user_input = input(prompt("which one do you mean: "))
        if not is_int(user_input):
            continue
        
        input_int = int(user_input)
        if input_int - 1 >= len(find_result):
            continue
        
        return find_result[input_int - 1]


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
        
            card.attributes[find_attribute(attr, value)] = value

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
