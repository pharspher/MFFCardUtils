#!/usr/bin/env python3

from IOUtils import read_card_data, save_card_data
from Utils import *


def verify_input_index(input_index):
    result = is_int(input_index)
    if not result:
        print_warn("invalid input")
        
    return result


def remove_card():
    card_data = read_card_data()

    input_index = get_input(prompt("Card index: "), verify_input_index)

    card_index = int(input_index)
    
    if card_index >= len(card_data):
        print_warn("card index out of range, abort!")
        return

    card = card_data[card_index]
    
    print(content("==========================="))
    print(content("Card: " + str(card.index)))
    print(content("---------------------------"))
    print_card(card)
    print(content("==========================="))

    answer = input(warn("remove[y, n]? "))

    if answer == "y":
        print_done("remove card " + str(card_index))
        del card_data[card_index]
        save_card_data(card_data)
    else:
        print_done("remove abort")
