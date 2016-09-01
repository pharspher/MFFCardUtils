#!/usr/bin/env python3

from colorama import Fore, Style


def print_card(card):
    for attribute in card.attributes.keys():
        print(content("{0:20}: {1}".format(attribute, card.attributes[attribute])))


def print_vector(vector):
    vector_string = "["
    for dimension_value in vector:
        vector_string += "{0:6.2f}".format(dimension_value) + ", "
    vector_string += "]"
    print(content(vector_string))


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
    
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_input(prompt, condition):
    done = False
    
    while not done:
        user_input = input(prompt)
        if condition(user_input):
            return user_input
        else:
            continue


def highlight(message):
    return Fore.YELLOW + message + Style.RESET_ALL


def warn(message):
    return Fore.RED + message + Style.RESET_ALL


def done(message):
    return Fore.GREEN + message + Style.RESET_ALL


def hint(message):
    return Fore.CYAN + message + Style.RESET_ALL


def prompt(message):
    return highlight(message)


def content(message):
    return Style.BRIGHT + message + Style.RESET_ALL


def print_warn(message):
    print(warn(message))
    
    
def print_done(message):
    print(done(message))


def print_highlight(message):
    print(highlight(message))
    
    
def seperate():
    print("===================================")
