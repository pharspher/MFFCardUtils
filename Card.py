#!/usr/bin/env python3


class Card:
    attribute_names = [
        "cooldown",
        "all_attack",
        "physical_attack",
        "energy_attack",
        "defense_ignore",
        "attack_speed",
        "critical_rate",
        "critical_damage",
        "movement_speed",
        "dodge",
        "recovery_rate",
        "cc_time",
        "phy_def",
        "ene_def",
        "all_def",
        "hp"]
    
    def __init__(self, index):
        self.attributes = {}
        self.index = index
        self.cardName = "Card-" + str(self.index)

