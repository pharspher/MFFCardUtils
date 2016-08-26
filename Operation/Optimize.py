#!/usr/bin/env python3

from itertools import combinations
from utils import read_card_data
from Card import Card


def get_vector_set(card_set):
    result_set = []
    for card in card_set:
        result_set.append(card.to_vector())

    return result_set


def sum_vectors(card_set):
    vectors = get_vector_set(card_set)

    sum_vector = []

    for dimension in range(len(Card.attribute_names)):
        dimension_sum = 0
        for vector in vectors:
            dimension_sum += vector[dimension]

        sum_vector.append(dimension_sum)

    return sum_vector


def print_attribute(vector):
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        if vector[index] == 0:
            continue
        print("{0:20}: {1:6.2f}".format(attribute, vector[index]))


def optimize():
    cards = read_card_data()

    vectors = []
    for card in cards:
        vectors.append(card.to_vector())

    card_set_list = []
    index_combs = combinations(range(len(vectors)), 5)

    for index_comb in index_combs:
        card_set = []
        for index in index_comb:
            card_set.append(cards[index])

        card_set_list.append(card_set)

    print("number of card combination: " + str(len(card_set_list)))

    print("============================")

    for card_set in card_set_list:
        vector = sum_vectors(card_set)
        cooldown_index = Card.attribute_names.index("cooldown")
        all_attack_index = Card.attribute_names.index("all_attack")
        ignore_index = Card.attribute_names.index("defense_ignore")

        if vector[cooldown_index] < 25:
            continue

        if vector[all_attack_index] < 20:
            continue

        if vector[ignore_index] < 5:
            continue

        card_list = ""
        for card in card_set:
            card_list = card_list + str(card.index) + ", "

        print("Cards: [" + card_list + "]")
        print("----------------------------")
        print_attribute(vector)
        print("============================")
