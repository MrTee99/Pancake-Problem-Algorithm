# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:17:44 2019

@author: MrTee
"""
import SearchStrategy;
from queue import Queue;

class BFS_Strategy(SearchStrategy.SearchStrategy):
    OPTIMAL = True;
    NODES_EXPANDED = 0; 
    
    def __init__(self):
        print("\n------------- IMPLEMENTING BREADTH FIRST SEARCH -------------");
        self.queue = Queue();
        # We are creating queue as our fringe list because BFS works in FIFO manner and so does Queue.
        
    def IsEmpty(self):
        return self.queue.empty();
        # This will return true if queue is empty else it will return false.
    
    def AddNode(self, node):
        return self.queue.put(node);
        # This will add the node in the queue at the first index (FIFO).
    
    def RemoveNode(self):
        BFS_Strategy.NODES_EXPANDED += 1;
        return self.queue.get();
        # This will return the first node in the queue as well as remove it from the queue (because of FIFO).

        