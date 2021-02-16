# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:36:59 2019

@author: MrTee
"""

from abc import abstractmethod;

class SearchState(object):
    
    @abstractmethod
    def __init__(self): pass
        # This is a constructor
 
    @abstractmethod
    def GetCurrentState(self): pass
        # This will help us get whatever our current state is
        # This is just a getter function

    @abstractmethod
    def GetAction(self): pass
        # This will tell us what action we took to get to our current state.
        # This is just a getter function

    @abstractmethod
    def GetCost(self): pass
        # This will tell us what was the cost to get to our current state.
        # This is just a getter function

    @abstractmethod
    def StringRep(self): pass
        # This will help us give a string representation to our current state.
        # So that if this state comes up again we would know that this is a duplicate state.
