# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:12:04 2019

@author: MrTee
"""
import Heuristic;

class PancakeHeuristic(Heuristic.Heuristic):
    
    def __init__(self, goal):
        self.goal = goal
        
    def CalculateHeuristic(self, state):
        heuristic = 0;
        
        for i in range (1, len(self.goal)+1):
            
            highestValue = self.goal[len(self.goal)-i];             # is se pata chal giya highest value jo abhi tak humne check nahi ki konsi ha
            csValuePosition = state.index(highestValue);            # ab humay yeh bhi pata chal giya kay highestValue humari current state ma kis position par ha
            
            if csValuePosition != self.goal.index(highestValue):    # Agar current state ma highest value ki position goal state kay highest value ki position kay barabar nahi ha to yehi hueristic value ha humari
                heuristic = highestValue;
                break;
            
        return heuristic;

    
    