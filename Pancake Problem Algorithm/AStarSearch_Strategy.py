# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 00:41:46 2019

@author: MrTee
"""

import SearchStrategy;
from queue import PriorityQueue;

class AStarSearch_Strategy(SearchStrategy.SearchStrategy):
    OPTIMAL = True;
    NODES_EXPANDED = 0;
    
    def __init__(self):
        print("\n------------- IMPLEMENTING A* SEARCH -------------");
        self.priorityQueue = PriorityQueue();
        # We are creating priority queue as our fringe list because Greedy works in a manner in which it selects state that has the lowest heuristic value and so does priority Queue. (Priority Queue consider 1 as high priority and 10 as low priority)
        
    def IsEmpty(self):
        return self.priorityQueue.empty();
        # This will return true if priority queue is empty else it will return false.
    
    def AddNode(self, node):
        return self.priorityQueue.put(((node.cost+node.heuristic), node));
        # This will add the node in the priority queue and it's heuristic value will be considered as it is high priority node or low priority node
    
    def RemoveNode(self):
        AStarSearch_Strategy.NODES_EXPANDED += 1;
        return  self.priorityQueue.get()[1];
        # This will return the node (not the heuristic value from the tupple example (0, <node object>)) which has the least heuristic value in the priority queue and it will also remove it from the priority queue.
        
    def Size(self):
        return self.priorityQueue.qsize();