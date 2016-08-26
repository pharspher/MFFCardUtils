#!/usr/bin/env python3

from GenerateCard import GenerateCard
from ListCards import ListCards
from Optimize import Optimize
from RemoveCard import RemoveCard

def printOptions():
    print()
    for key in commandOperations.keys():
        print(key + ": " + commandOperations[key].__class__.__name__)

commandOperations = {"a": GenerateCard(), "l": ListCards(), "o": Optimize(5), "r": RemoveCard()}

done = False

while (done == False):
    printOptions()
    inputCommand = input("what do you want: ").strip()
    
    if (inputCommand == "q"):
        print("Thank you, bye!")
        done = True
        
    elif commandOperations.__contains__(inputCommand):
        print()
        commandOperations.get(inputCommand).run()
        
    else:
        print("command not found\n")
        continue