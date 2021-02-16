# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:13:05 2019

@author: MrTee
"""

import SearchProblem;
import PancakeSearchState;
import PancakeHeuristic;

# This class inherits SearchProblem abstarct class and it will implement it's abstract methods over here.
class PanckaeSearchProblem(SearchProblem.SearchProblem):
    
    def __init__(self, initialState, goalState):
        self._initialState = PancakeSearchState.PanckaeSearchState(initialState, 0, 0, PancakeHeuristic.PancakeHeuristic(goalState).CalculateHeuristic(initialState));
        self._goalState = goalState;
        
        # Here we are setting the state of our initialState list which is stored in a private variable = _initialState
        # Here we are assigning what is our goal that we want to achieve in a private variable = _goalState
        
    def InitialState(self):
        return self._initialState;
    
        # Here we are simply returning our initial state. You can call it a getter method.
        
    def IsGoal(self, currentState):
        cs = currentState.GetCurrentState();
        if cs == self._goalState:
            return True;
        else:
            return False;
        
        # Here first we get ourselves entire currentState of the list
        # Then we compared both goalState list and currentState list to check if both are identical
        # If yes then we returned true else we returned that currentState is not our goalState
        
    def SuccessorFunction(self, currentState):
        nextPossibleStates = [];
        cs = currentState.GetCurrentState();
        
        # Getting all possible successor states of our current state / flipping the pancakes.
        for flipPoint in range(1, len(cs)):
            newState = [];
            for items in range(len(cs)-flipPoint, -1, -1):
                newState.append(cs[items]); 
                
            if (len(newState) != len(cs)):
                for items in range(len(newState), len(cs)):
                    newState.append(cs[items]);
            
            ns = PancakeSearchState.PanckaeSearchState(newState, flipPoint, ((len(cs)+1)-flipPoint), PancakeHeuristic.PancakeHeuristic(self._goalState).CalculateHeuristic(newState));
            nextPossibleStates.append(ns);

        return nextPossibleStates;
        
        # nextPossibleStates = It will be used to hold all possible successors of our currentState.
        # newState = We are creating N-1 newstates that will be the successors of our currentState. (N is numOfPancakes / length of currentState)
        # Action = flipPoint (means that from whichever place we are flipping our pancakes will be our action)
        # Cost =  (len(cs)+1)-flipPoint (Ex: (5+1)-1 = 5 means that if we take action=1 it will flip all 5 pancakes which means cost will be 5)
        
        """
            initial list = [2, 4, 1, 5, 3]
            goal list = [1, 2, 3, 4, 5]
            
            SUCCESSOR FUCNTIONS OF INITIAL LIST
            - [3, 5, 1, 4, 2]  we have flipped 3 or index = 4 (flipPoint)
            - [5, 1, 4, 2, 3]  we have flipped 5 or index = 3 (flipPoint)
            - [1, 4, 2, 5, 3]  we have flipped 1 or index = 2 (flipPoint)
            - [4, 2, 1, 5, 3]  we have flipped 4 or index = 1 (flipPoint)
            
            means we have to flip like this:
                - First get length of the list n (e.g: n = 5)
                - Now we will run a loop from i = 1 to i < n
                - first flip will be: Flip list from index n-i (e.g: 5-1 = 4)
                - Second flip will be: Flip list from index n-i (e.g: 5-2 = 3)
                - ......
                - ........
                - At last flip will be: Flip list from index n-i (e.g: 5-4 = 1)
                
            DETERMINING HOW TO GET COST:
                
                initial list = [1, 2, 3, 4, 5]
                
                if flipPoint = 1, we have flipped [5, 4, 3, 2, 1], then list will be = [5, 4, 3, 2, 1], so cost = 5
                if flipPoint = 2, we have flipped [4, 3, 2, 1], then list will be = [4, 3, 2, 1, 5], so cost = 4
                if flipPoint = 3, we have flipped [3, 2, 1], then list will be = [3, 2, 1, 4, 5], so cost = 3
                if flipPoint = 4, we have flipped [2, 1], then list will be = [2, 1, 3, 4, 5], so cost = 2
            
            LIST KO KAHI SE BHI REVERSE/FLIP KARNAY KA CODE
            
                    a = [1,2,3,4,5]
                    b=[]
                    flipPoint =  This number will tell where I am putting spatula in the plate. (It should always be less than len(a))

                    for flipPoint in range(1, len(a)):
                        #print(flipPoint)
                        for items in range(len(a)-flipPoint, -1, -1):
                            b.append(a[items]); 
    
                        if (len(b) != len(a)):
                            for items in range(len(b), len(a)):
                                b.append(a[items]);
            
                        #print(b);
                        #print("cost: %d" %((len(a)+1)-flipPoint));
                        #b = [];
 
            
        """
        
        
        
        
        
        
        
        
        
        
        