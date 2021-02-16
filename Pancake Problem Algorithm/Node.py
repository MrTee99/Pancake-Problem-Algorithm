# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:29:31 2019

@author: MrTee
"""

class Node(object):
    
    def __init__(self, state, parentNode=None, depth=0, cost=0, action=0, heuristic=0):
        self.state = state;
        self.parentNode = parentNode;
        self.depth = depth;
        self.cost = cost;
        self.action = action;
        self.heuristic = heuristic;

    def __lt__(self, other):
        return self.cost < other.cost
        # This method is useful in UCS when two nodes have same cost so this method will tell priority queue to consider that current node has more priority over the other node that have same cost(priority value).        