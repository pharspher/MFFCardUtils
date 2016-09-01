#!/usr/bin/env python3

from itertools import combinations
from Card import Card
from colorama import Fore, Style
from Utils import print_warn, hint, prompt, is_int


def get_attribute_vector(card):
    attribute_name_to_attribute_value = lambda attribute_name: float(card.attributes[attribute_name]) if attribute_name in card.attributes.keys() else 0
    return list(map(attribute_name_to_attribute_value, card.attribute_names))


def get_attribute_vector_list(card_set):
    return list(map(lambda card: get_attribute_vector(card), card_set))


def get_summed_attribute_vector(card_set):
    attribute_vector_list = get_attribute_vector_list(card_set)
    indexes = range(len(attribute_vector_list))

    sum_attribute_vector = []

    for dimension in range(len(Card.attribute_names)):
        dimension_sum = 0
        
        for attribute_vector in attribute_vector_list:
            dimension_sum += attribute_vector[dimension]

        sum_attribute_vector.append(dimension_sum)

    return sum_attribute_vector


# c(5, 3) = [[0, 1, 2], [0, 1, 3], ...] => [[card0, card1, card2], [card0, card1, car3], ...]
def get_card_set_combination(cards):
    card_index_combinations = combinations(range(len(cards)), 5)

    # lambda: 0 -> card_0
    index_to_card = lambda index: cards[index]
    
    # lambda: [0, 1, 2] -> [card_0, card_1, card_2]
    index_list_to_card_list = lambda index_list: list(map(index_to_card, index_list))

    return list(map(index_list_to_card_list, card_index_combinations))


def print_attribute(vector):
    for attribute in Card.attribute_names:
        index = Card.attribute_names.index(attribute)
        if vector[index] == 0:
            continue
        print("{0:20}: {1:6.2f}".format(attribute, vector[index]))


def compare_card_set(card_set1, card_set2):
    sum1 = get_summed_attribute_vector(card_set1)
    sum2 = get_summed_attribute_vector(card_set2)
    
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
    from IOUtils import read_card_data
    cards = read_card_data()
    compare_card_set([cards[0], cards[1], cards[2], cards[3], cards[4]], card_set)


def contain_exclusive_card(card_set):
    from IOUtils import read_exclusive_group
    ex_groups = read_exclusive_group()
    
    for group in ex_groups:
        count = 0
        for card in card_set:
            if group.__contains__(card.index):
                count += 1
                if count >= 2:
                    return True
    return False


def resolve_attribute_name(input_attribute, input_value, interactive_resolve=True):
    find_result = []
    
    for attribute_name in Card.attribute_names:
        if attribute_name.startswith(input_attribute):
            find_result.append(attribute_name)
    
    if len(find_result) == 0:
        return None
    
    if len(find_result) == 1:
        return find_result[0]
        
    print_warn("ambiguous: " + input_attribute + " " + str(input_value))
    
    if not interactive_resolve:
        return None
        
    option_string = ""    
    for i in range(len(find_result)):
        option_string += (str(i + 1) + ". " + find_result[i] + ", ")
    
    print(hint(option_string))
    
    done = False
    
    while not done:
        user_input = input(prompt("which one do you mean: "))
        if not is_int(user_input):
            continue
        
        input_int = int(user_input)
        if input_int - 1 >= len(find_result):
            continue
        
        return find_result[input_int - 1]