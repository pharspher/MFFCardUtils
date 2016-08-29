#!/usr/bin/env python3

from IOUtils import read_card_data, save_card_data
from Utils import print_card


def remove_card():
    card_data = read_card_data()

    input_index = input("Card index: ")

    if not is_int(input_index):
        print("invalid input")
        return

    card_index = int(input_index)

    if card_index >= len(card_data):
        print("card index out of range")
        return

    card = card_data[card_index]
    print("===========================")
    print("Card: " + str(card.index))
    print("---------------------------")
    print_card(card)
    print("===========================")

    answer = input("remove[y, n]? ")

    if answer == "y":
        print("remove card " + str(card_index))
        del card_data[card_index]
        save_card_data(card_data)
    else:
        print("remove abort")


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False