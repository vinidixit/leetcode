#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:14:31 2020

@author: vdixit
"""

import collections

class Solution: # TOPOLOGICAL SORTING
    
    # detect cycle
    def detect_cycle(self, current, visited, dependents):
        #if current not in prerequisites:
        #    return True
        
        print(current, visited)
        if current in visited:
            return False
        
        visited.add(current) # dont add the one, not having any prerequisite
        
        for d in dependents[current]:
            if not self.detect_cycle(d, visited, dependents):
                return False
        
        visited.remove(current) # After path is traversed, clear it for other independents (siblings)
        
        return True
            
        
    def canFinish(self, numCourses, prerequisites):
        
        prerequisites_map = collections.defaultdict(set)
        indegrees = set(range(numCourses))
        dependents = collections.defaultdict(set)
        
        for n, p in prerequisites:
            if n == p: # cycle
                return False
            prerequisites_map[n].add(p) # directed graph
            dependents[p].add(n)
            
            if n in indegrees:
                indegrees.remove(n)
        
        if len(indegrees) == 0:
            return False
        
        print(dependents)
        for parent in indegrees:
            visited = set()
            if not self.detect_cycle(parent, visited, dependents):
                return False
        
        return True

N = 7
prereqs = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

print(Solution().canFinish(N, prereqs))

### INCOMPLETE / INCORRECT

        