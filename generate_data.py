#!/usr/bin/env python3

from Operation.GenerateCard import generate_card
from Operation.ListCards import list_cards
from Operation.Optimize import optimize
from Operation.RemoveCard import remove_card
from Operation.InsertCard import insert_card
from Utils import *


command_operations = {
    "a": generate_card,
    "l": list_cards,
    "o": optimize,
    "r": remove_card,
    "i": insert_card
}


def print_options():
    print()
    seperate()
    for key in command_operations.keys():
        print(hint(str(key) + ": " + str(command_operations[key].__name__)))


done = False

while not done:
    print_options()
    input_command = input(highlight("what do you want: ")).strip()
    
    if input_command == "q":
        print_done("Thank you, bye!")
        done = True
        
    elif command_operations.__contains__(input_command):
        print()
        command_operations.get(input_command)()
        
    else:
        print_warn("command not found\n")
        continue
