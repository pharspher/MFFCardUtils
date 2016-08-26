#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Operation(metaclass = ABCMeta):
    
    @abstractmethod
    def run(self):
        print("run")
    