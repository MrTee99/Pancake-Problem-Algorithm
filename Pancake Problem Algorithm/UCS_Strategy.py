# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 23:54:49 2019

@author: MrTee
"""

import SearchStrategy;
from queue import PriorityQueue;

class UCS_Strategy(SearchStrategy.SearchStrategy):
    OPTIMAL = True;
    NODES_EXPANDED = 0;
    
    def __init__(self):
        print("\n------------- IMPLEMENTING UNIFORM COST SEARCH -------------");
        self.priorityQueue = PriorityQueue();
        # We are creating priority queue as our fringe list because UCS works in a manner in which it selects state that has the lowest cost and so does priority Queue. (Priority Queue consider 1 as high priority and 10 as low priority)
        
    def IsEmpty(self):
        return self.priorityQueue.empty();
        # This will return true if priority queue is empty else it will return false.
    
    def AddNode(self, node):
        return self.priorityQueue.put((node.cost, node));
        # This will add the node in the priority queue and it's cost will be considered as it is high priority node or low priority node
    
    def RemoveNode(self):
        UCS_Strategy.NODES_EXPANDED += 1;
        return self.priorityQueue.get()[1];
        # This will return the node (not the cost from the tupple example (0, <node object>)) which has the least cost in the priority queue and it will also remove it from the priority queue.
        