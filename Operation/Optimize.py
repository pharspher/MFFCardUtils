#!/usr/bin/env python3

from itertools import combinations
from IOUtils import read_card_data, read_exclusive_group
from Card import Card
from Utils import get_card_vector
from colorama import Fore, Back, Style


def get_vector_set(cards):
    result_set = []
    for card in cards:
        result_set.append(get_card_vector(card))

    return result_set


def sum_card_set_vectors(card_set):
    vectors = get_vector_set(card_set)

    sum_vector = []

    for dimension in range(len(Card.attribute_names)):
        dimension_sum = 0
        for vector in vectors:
            dimension_sum += vector[dimension]

        sum_vector.append(dimension_sum)

    return sum_vector


def get_card_set_combination(cards):
    card_set_list = []
    index_combs = combinations(range(len(get_vector_set(cards))), 5)

    for index_comb in index_combs:
        card_set = []

        for index in index_comb:
            card_set.append(cards[index])

        card_set_list.append(card_set)

    return card_set_list


def print_attribute(vector):
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        if vector[index] == 0:
            continue
        print("{0:20}: {1:6.2f}".format(attribute, vector[index]))


def compare_card_set(card_set1, card_set2):
    sum1 = sum_card_set_vectors(card_set1)
    sum2 = sum_card_set_vectors(card_set2)
    
    for attribute_name in Card.attribute_names:
        index = Card.attribute_names.index(attribute_name)
        
        value1 = sum1[index]
        value2 = sum2[index]
        
        color = Style.RESET_ALL
        if value1 > value2:
            color = Fore.RED
        elif value2 > value1:
            color = Fore.GREEN
        
        difference = value2 - value1
        
        print(("{0:20}: {1:6.2f}  -> " + color + "{2:6.2f} ({3:6.2f})" + Style.RESET_ALL).format(attribute_name, sum1[index], sum2[index], difference))
    

def compare_with_current_card_set(card_set):
    cards = read_card_data()
    compare_card_set([cards[0], cards[1], cards[2], cards[3], cards[4]], card_set)


def contain_exclusive_card(card_set):
    ex_groups = read_exclusive_group()
    
    for group in ex_groups:
        count = 0
        for card in card_set:
            if group.__contains__(card.index):
                count += 1
                if count >= 2:
                    return True
    return False


def optimize():
    cards = read_card_data()
    card_set_combinations = get_card_set_combination(cards)

    print("number of card combination: " + str(len(card_set_combinations)))

    print("============================")

    for card_set in card_set_combinations:
        sum_vector = sum_card_set_vectors(card_set)

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
