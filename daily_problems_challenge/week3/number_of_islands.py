#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:36:37 2020

@author: vdixit
"""


grid = [["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]

grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]


import numpy as np

class Solution:
    def cover(self, grid, r, c, ROW, COL, visited):
        if r < 0 or r >= ROW or c < 0 or c >= COL or visited[r][c] or grid[r][c] == '0':
            return 
        
        print(r, c, grid[r][c], visited[r][c])

        visited[r][c] = True
        
        self.cover(grid, r+1, c, ROW, COL, visited)
        self.cover(grid, r, c+1, ROW, COL, visited)
        self.cover(grid, r-1, c, ROW, COL, visited)
        self.cover(grid, r, c-1, ROW, COL, visited)
        
    def numIslands(self, grid: list) -> int:
        count = 0
        ROW, COL = len(grid), len(grid[0])
        visited = np.zeros((ROW, COL), dtype=bool)
        i,j = 0,0
        
        
        for i in range(ROW):
            for j in range(COL):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    print(count)
                    self.cover(grid, i, j, ROW, COL, visited)
        
        return count
    

print(Solution().numIslands(grid))
        