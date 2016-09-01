#!/usr/bin/env python3

from IOUtils import read_card_data, read_exclusive_group
from Operation.Utils import *
from colorama import Fore, Back, Style
import os


def optimize():
    cards = read_card_data()
    card_set_combinations = get_card_set_combination(cards)

    print("number of card combination: " + str(len(card_set_combinations)))

    print("============================")

    for card_set in card_set_combinations:
        sum_vector = get_summed_attribute_vector(card_set)

        cooldown_index = Card.attribute_names.index("cooldown")
        all_attack_index = Card.attribute_names.index("all_attack")
        ignore_index = Card.attribute_names.index("defense_ignore")

        if sum_vector[cooldown_index] < 25:
            continue

        if sum_vector[all_attack_index] < 20:
            continue

        if sum_vector[ignore_index] < 5:
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
