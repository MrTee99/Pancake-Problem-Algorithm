# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:16:31 2019

@author: MrTee
"""

import SearchState;

# This class inherits SearchState abstarct class and it will implement it's abstract methods over here.
class PanckaeSearchState(SearchState.SearchState):
    
    def __init__(self, currentState, action, cost, heuristic):
        self.currentState = currentState;
        self.action = action;
        self.cost = cost;
        self.heuristic = heuristic;
        self.string = None;
        
        # We will get values of currentState, action and cost through the constructor and,
        # In constructor we will create a public variable of currentState, action and cost and we will assign these new variables the values that we got through constructor.
        # self.string = nameOfTheState. (self.String will be used to assign every state a unique name which will be useful later on to check when we get a duplicate state.
        
    def GetCurrentState(self):
        return self.currentState;
    
    def GetAction(self):
        return self.action;
    
    def GetCost(self):
        return self.cost;
    
    def GetHeuristic(self):
        return self.heuristic;
    
    def StringRep(self):
        if self.string is None:
            stateName = '';
            for item in range(0, len(self.currentState)):
                stateName = stateName + str(self.currentState[item]);
            self.string = stateName;
            
        return self.string;
        
        # I am going to represent the name of my state by getting all the values and convert them into string.
        # Example: List = [1,2,3,4,5], State Name will be '12345'
        
        '''
        CODE TESTING IMPLEMENTATION:
            
            a = [1,2,3,4,5]
            stateName = '';

            for item in range(0, len(a)):
                stateName = stateName + str(a[item]);

            print(stateName)
        '''
            