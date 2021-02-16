# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:10:56 2019

@author: MrTee
"""

from abc import abstractmethod;

class SearchStrategy(object):
    
    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def IsEmpty(self): pass
        # This will be used to check weather the fringe list is empty or not

    @abstractmethod
    def AddNode(self, node): pass
        # This will be used to add a node in the fringe list

    @abstractmethod
    def RemoveNode(self): pass
        # This will be used to remove a node in the fringe list