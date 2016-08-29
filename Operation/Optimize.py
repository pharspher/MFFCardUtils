#!/usr/bin/env python3

from itertools import combinations
from IOUtils import read_card_data
from Card import Card
from Utils import get_card_vector


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

        card_list = ""
        for card in card_set:
            card_list = card_list + str(card.index) + ", "

        print("Cards: [" + card_list + "]")
        print("----------------------------")
        print_attribute(sum_vector)
        print("============================")
