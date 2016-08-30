#!/usr/bin/env python3

from Card import Card
from IOUtils import read_card_data, save_card_data
from Utils import print_card, is_int, get_input, print_warn
from Operation.GenerateCard import create_new_card


def print_options():
    print()
    hint = ""
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        hint = hint + str(index) + ". " + attribute + "\n"
    print(hint)


def find_attribute(input_attribute, input_value):
    find_result = []
    
    for attribute_name in Card.attribute_names:
        if attribute_name.startswith(input_attribute):
            find_result.append(attribute_name)
    
    if len(find_result) == 1:
        return find_result[0]
        
    print("ambiguous: " + input_attribute + " " + str(input_value))
        
    option_string = ""    
    for i in range(len(find_result)):
        option_string += (str(i + 1) + ". " + find_result[i] + ", ")
    
    print(option_string)
    
    done = False
    
    while not done:
        user_input = input("which one do you mean: ")
        if not is_int(user_input):
            continue
        
        input_int = int(user_input)
        if input_int - 1 >= len(find_result):
            continue
        
        return find_result[input_int - 1]


def verify_index(input_index):
    return is_int(input_index)


def insert_card():
    card = create_new_card()
    
    if card == None:
        return
    
    index = int(get_input("insert at index: ", verify_index))
    
    card_data = read_card_data()
    
    if index <= len(card_data):
        card_data.insert(index, card)
        save_card_data(card_data)
    else:
        print_warn("invalid index, cancel!")

