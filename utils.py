#!/usr/bin/env python3

from Card import Card


def read_card_data(file_name = "cards_data"):
    with open(file_name) as file:
        lines = file.readlines()

    card_list = []

    card_count = 0

    for raw_line in lines:
        line = raw_line.strip()

        if line == "#card":
            card = Card(card_count)
            card_list.append(card)
            card_count += 1

        else:
            attribute = line.split(":")

            if len(attribute) != 2:
                continue
            else:
                card_list[-1].attributes[attribute[0].strip()] = attribute[1].strip()

    return card_list


def save_card_data(card_data, file_name = "cards_data"):
    with open(file_name, "w") as file:
        for card in card_data:
            print("#card", file)

            for attribute in card.attributes.keys():
                print(attribute + ": " + card.attributes[attribute], file)

            print("\n", file)


def print_vector(vector):
    vector_string = "["
    for dimension_value in vector:
        vector_string += "{0:6.2f}".format(dimension_value) + ", "
    vector_string += "]"
    print(vector_string)