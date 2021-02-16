# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:34:23 2019

@author: MrTee
"""

import Node;
import PancakeSearchProblem;
import BFS_Strategy;
import DFS_Strategy;
import UCS_Strategy;
import GreedySearch_Strategy;
import AStarSearch_Strategy;

class Search(object):
    
    def __init__(self, searchProblem, searchStrategy):
        self.searchProblem = searchProblem;
        self.searchStrategy = searchStrategy;
        
    def SolveProblem(self):
        initialNode = Node.Node(self.searchProblem.InitialState(), None, 0, 0, 0, self.searchProblem.InitialState().GetHeuristic());
        self.searchStrategy.AddNode(initialNode);
        
        duplicateMap = {};
        duplicateMap[initialNode.state.StringRep()] = initialNode.state.StringRep();
        
        result = None;

        while not self.searchStrategy.IsEmpty():
            currentNode = self.searchStrategy.RemoveNode();
            
            if self.searchProblem.IsGoal(currentNode.state):
                result = currentNode;
                break;
            
            nextPossibleStates = self.searchProblem.SuccessorFunction(currentNode.state);
            
            for nextState in nextPossibleStates:
                if nextState.StringRep() not in duplicateMap:
                    newNode = Node.Node(nextState, currentNode, currentNode.depth + 1, currentNode.cost + nextState.cost, nextState.action, nextState.heuristic);
                    self.searchStrategy.AddNode(newNode);
                    duplicateMap[newNode.state.StringRep()] = newNode.state.StringRep();
        
                    
        return result;
    
    def PrintResult(self, result):
        if result.parentNode is None:
            print("\n  Initial State is: %s" % result.state.GetCurrentState());
            print("  Sorting is started...");
            return;
        self.PrintResult(result.parentNode);
        print("\n  flipped the pancake from %dth position" %result.action);
        print("       New State is: %s" % result.state.GetCurrentState());
        print("       cost of the flip = %d" %result.cost);
        print("       heuristic value = %d" %result.heuristic);
        

if __name__ == "__main__":
    searchProblem = PancakeSearchProblem.PanckaeSearchProblem([4, 1, 2, 3], [1, 2, 3, 4]);
    #searchStrategy = AStarSearch_Strategy.AStarSearch_Strategy();     # WORKING
    #searchStrategy = GreedySearch_Strategy.GreedySearch_Strategy();   # WORKING
    #searchStrategy = UCS_Strategy.UCS_Strategy();                     # WORKING
    #searchStrategy = DFS_Strategy.DFS_Strategy();                     # WORKING
    searchStrategy = BFS_Strategy.BFS_Strategy();                      # WORKING
    search = Search(searchProblem, searchStrategy);
    result = search.SolveProblem();
    
    if searchStrategy.OPTIMAL:
        print("\n1). FOLLOWING SOLUTION IS AN OPTIMAL SOLUTION");
    else:
        print("\n1). FOLLOWING SOLUTION IS NOT AN OPTIMAL SOLUTION");
    
    print("2). NUMBER OF NODES EXPANDED = ", searchStrategy.NODES_EXPANDED);
    print("3). SOLUTION:-");
    
    if result is not None:
        search.PrintResult(result);
        
    
    
    
    
    
    
    
    
    