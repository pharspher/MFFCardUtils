#!/usr/bin/env python3


def print_card(card):
    for attribute in card.attributes.keys():
        print("{0:20}: {1}".format(attribute, card.attributes[attribute]))


def print_vector(vector):
    vector_string = "["
    for dimension_value in vector:
        vector_string += "{0:6.2f}".format(dimension_value) + ", "
    vector_string += "]"
    print(vector_string)


def get_card_vector(card):
    vector = []

    for attrName in card.attribute_names:
        if attrName in card.attributes:
            vector.append(float(card.attributes[attrName]))

        else:
            vector.append(0)

    return vector


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
