#!/usr/bin/env python3

class Card:
    attributeIndex = [
        "attack_speed",
        "defense_ignore",
        "cooldown",
        "all_attack",
        "physical_attack",
        "energy_attack",
        "movement_speed",
        "critical_rate",
        "critical_damage",
        "dodge",
        "recovery_rate"]
    
    def __init__(self, index):
        self.attributes = {}
        self.index = index
        self.cardName = "Card-" + str(self.index)
    
    def print(self):
        for attribute in self.attributes.keys():
            print("{0:20}: {1}".format(attribute, self.attributes[attribute]))
            
    def toVector(self):
        vector = []
        
        for attrName in self.attributeIndex:
            if attrName in self.attributes:
                vector.append(float(self.attributes[attrName]))
                
            else:
                vector.append(0)
                
        return vector