#!/usr/bin/env python3

from Card import Card
from IOUtils import read_card_data, save_card_data
from Utils import print_card, is_int, get_input, print_warn
from Operation.GenerateCard import create_new_card


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
        print_warn("invalid index, abort!")

