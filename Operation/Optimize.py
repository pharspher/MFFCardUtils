#!/usr/bin/env python3

from Operation.Utils import *
from IOUtils import read_card_data, read_exclusive_group
from Operation.Utils import *
from colorama import Fore, Back, Style
import os


def optimize():
    cards = read_card_data()
    card_set_combinations = get_card_set_combination(cards)

    print("number of card combination: " + str(len(card_set_combinations)))

    print("============================")

    equipped_card_set = list(map(lambda index: cards[index], range(5)))
    equipped_card_attr = get_summed_attribute_vector(equipped_card_set)
    
    important_attr_index = range(5)

    for card_set in card_set_combinations:
        sum_vector = get_summed_attribute_vector(card_set)

        skip = False
        for index in important_attr_index:
            if sum_vector[index] < equipped_card_attr[index]:
                skip = True
                break

        if skip:
            continue

        if contain_exclusive_card(card_set):
            continue

        card_list = ""
        for i in range(len(card_set)):
            if i == 0:
                card_list += str(card_set[i].index)
            else:
                card_list += ", " + str(card_set[i].index)

        print("Cards: [" + card_list + "]")
        print("----------------------------")
        #print_attribute(sum_vector)
        compare_with_current_card_set(card_set)
        print("============================")
