# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 23:18:50 2019

@author: MrTee
"""

import SearchStrategy;

class DFS_Strategy(SearchStrategy.SearchStrategy):
    OPTIMAL = False;
    NODES_EXPANDED = 0;
    
    def __init__(self):
        print("\n------------- IMPLEMENTING DEPTH FIRST SEARCH -------------");
        self.stack = [];
        # We are creating list as our fringe list because DFS works in LIFO manner and so does built-in python list.
        
    def IsEmpty(self):
        return self.stack == [];
        # This will return true if List/Stack is empty else it will return false.
    
    def AddNode(self, node):
        return self.stack.append(node);
        # This will add the node in the List at the last empty index (LIFO).
    
    def RemoveNode(self):
        DFS_Strategy.NODES_EXPANDED += 1;
        return self.stack.pop();
        # This will pop the top value in the list/stack and return it (because of LIFO).
