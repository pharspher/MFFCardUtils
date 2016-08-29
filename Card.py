#!/usr/bin/env python3


class Card:
    attribute_names = [
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

