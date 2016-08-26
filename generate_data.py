#!/usr/bin/env python3

from GenerateCard import GenerateCard
from ListCards import ListCards
from Optimize import Optimize

commandOperations = {"a": GenerateCard(), "l": ListCards(), "o": Optimize(5)}
print("\n")

done = False

while (done == False):
    inputCommand = input("what do you want: ").strip()
    
    if (inputCommand == "q"):
        print("Thank you, bye!")
        done = True
        
    elif commandOperations.__contains__(inputCommand):
        commandOperations.get(inputCommand).run()
        
    else:
        print("command not found\n")
        continue
