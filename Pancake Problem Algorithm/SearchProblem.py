# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:28:11 2019

@author: MrTee
"""

from abc import abstractmethod;

class SearchProblem(object):
    
    @abstractmethod
    def __init__(self): pass
         # This is a constructor
    
    @abstractmethod
    def InitialState(self): pass
        # This will be used to get whatever our initial state was.
         
    @abstractmethod
    def IsGoal(self, currentState): pass
        # This will be used to check if our current state is equal to our goal state or not
        
    @abstractmethod
    def SuccessorFunction(self, currentState): pass
        # This function will be used to find every possible successor of our current state
       
        