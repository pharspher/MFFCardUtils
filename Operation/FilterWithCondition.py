#!/usr/bin/env python3

from Operation.Utils import *
from Card import Card
from IOUtils import read_card_data, save_card_data
from Utils import *
from colorama import Style
import collections
import curses


def parse_condition(input_condition):
    split_input = input_condition.strip().split(" ")
    
    if len(split_input) == 0:
        return {}
    
    conditions = collections.OrderedDict()
    
    done = False
    index = 0
    
    while not done:
        if index + 1 >= len(split_input):
            break
        
        if not is_number(split_input[index + 1]):
            index += 1
            continue
        
        float_value = float(split_input[index + 1])
        
        found_attribute = resolve_attribute_name(split_input[index], split_input[index + 1])
        
        if found_attribute == None:
            index += 1
            continue
        
        conditions[found_attribute] = float_value
        
        index += 2
    
    return conditions


def match_conditions(card_set, conditions):
    if len(conditions.keys()) == 0:
        return False
    
    sum_vector = get_summed_attribute_vector(card_set)
    
    for attribute in conditions.keys():
        value = conditions[attribute]
        index = Card.attribute_names.index(attribute)
        
        if sum_vector[index] < value:
            return False
        
    return True


def print_max(conditions, card_set_combinations):
    filter_combinations = []
    for card_set in card_set_combinations:
        if contain_exclusive_card(card_set):
            continue
        filter_combinations.append(card_set)
        
    
    summed_vectors = list(map(get_summed_attribute_vector, filter_combinations))
    
    for attribute in conditions.keys():
        index = Card.attribute_names.index(attribute)
        
        max_value  = 0
        for vector in summed_vectors:
            if vector[index] > max_value:
                max_value = vector[index]
        
        print(Style.BRIGHT + hint("{0:20}: {1}".format(attribute, max_value)))


def find_best_card_set_with_conditions(card_sets, conditions):
    return {}


def filter_with_condition():
    done = False
    
    while not done:
        input_condition = input(prompt("condition: "))
        
        if len(input_condition.strip()) == 0:
            done = True
            print(warn("empty input, abort"))
            continue
        
        conditions = parse_condition(input_condition)
        
        print(Style.BRIGHT + hint("filter conditions: " + str(conditions)) + Style.RESET_ALL)
        
        if len(conditions.keys()) == 0:
            print(warn("no available condition found, press ENTER to abort"))
            continue
        
        cards = read_card_data()
        card_set_combinations = get_card_set_combination(cards)
    
        #for card_set in card_set_combinations:
        
        print_max(conditions, card_set_combinations)
        
        print("number of card combination: " + str(len(card_set_combinations)))
    
        print("============================")
    
        match_card_set = []
        match_count = 0
        for card_set in card_set_combinations:
            if not match_conditions(card_set, conditions):
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
            compare_with_current_card_set(card_set)
            print("============================")
            match_card_set.append(card_set)
            match_count += 1
            
        print_done("matched result: " + str(match_count))
        
        best_card_set = find_best_card_set_with_conditions(match_card_set, conditions)

