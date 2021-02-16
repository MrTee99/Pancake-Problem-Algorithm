# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 01:49:46 2019

@author: MrTee
"""

from abc import abstractmethod;

class Heuristic(object):
    
    @abstractmethod
    def __init__(self): pass
    
    @abstractmethod
    def CalculateHeuristic(state): pass
        # This will be used to calculate heuristics value of any given list (state)
         