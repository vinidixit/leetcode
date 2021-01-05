#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:33:03 2020

@author: vdixit
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution: 
    
    # O(ROW + COL)
    def staircase_search(self, matrix, ROW, COL):
        i, j = 0, COL-1 # TOP RIGHT
        res = -1
        while i < ROW and j >= 0:
            if matrix.get(i, j) == 1:
                res = j
                j -= 1
            else:
                i += 1
        return res
    
    
    ## O(ROW * log(COL)
    def contains_one(self, matrix, ROW, col):
        for i in range(ROW):
            if matrix.get(i, col) == 1:
                return True
        return False
    
    def binary_search(self, sorted_matrix, ROW, COL):
        l, r = 0, COL-1
        res = -1
        
        while l <= r:
            m = l + (r-l)//2 # left index is preferred
            if self.contains_one(sorted_matrix, ROW, m):
                res = m
                r = m-1
            else:
                l = m+1
        return res
                
            
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROW, COL = binaryMatrix.dimensions()
        
        if ROW == 0:
            return -1
        
        #ROW, COL = len(binaryMatrix), len(binaryMatrix[0])
        return self.binary_search(binaryMatrix, ROW, COL)