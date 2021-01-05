#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:20:23 2020

@author: vdixit
"""


import numpy as np

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        ROW, COL = len(matrix), len(matrix[0])
        
        matrix = np.asarray([[int(s) for s in row] for row in matrix]) # IMP CODE: Remember
        
        max_sq = np.max(matrix) # IMP boundary condition for [0], [0,0,0] : are at zeroth row/col
        
        sums_dp = np.zeros((ROW, COL), dtype = int) 
        sums_dp[0] = matrix[0]
        sums_dp[:,0] = matrix[:,0]
        
        # preprocessing
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] == 0:
                    continue
                    
                sums_dp[r][c] = min(sums_dp[r-1][c], sums_dp[r][c-1], sums_dp[r-1][c-1]) + 1
                max_sq = max(max_sq, sums_dp[r][c])
        
        return max_sq*max_sq
        
        """ OLD CODE 
        col_dp = np.zeros((ROW, COL), dtype = int)
        row_dp = np.zeros((ROW, COL), dtype = int)
        
        col_dp[0] = matrix[0]
        # preprocessing
        for c in range(COL):
            for r in range(1, ROW):
                if matrix[r][c] == 1:
                    col_dp[r][c] = col_dp[r-1][c] + 1
                # leave it zero, if zero | break the seq
        
        row_dp[:,0] = matrix[:,0]
        for r in range(ROW):
            for c in range(1, COL):
                if matrix[r][c] == 1:
                    row_dp[r][c] = row_dp[r][c-1] + 1
        
        max_possible_size = min(ROW, COL)
        max_size = 1
        
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    continue
                
                for size in range(max_size, max_possible_size):
                    if r+size >= ROW or c+size >= COL:
                        break
                    
                    cond1 =  col_dp[r+size][c] >= size+1 and row_dp[r][c+size] >= size+1 # check p2, p3
                    cond2 =  col_dp[r+size][c+size] >= size+1 and row_dp[r+size][c+size] >= size+1
                    
                    if cond1 and cond2:
                        max_size = size+1 # also start with next size
                        break
        return max_size*max_size
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(Solution().maximalSquare(matrix))