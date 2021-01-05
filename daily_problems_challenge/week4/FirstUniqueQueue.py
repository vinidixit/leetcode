#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:17:34 2020

@author: vdixit
"""


from collections import deque # remember
from collections import Counter

class FirstUnique:

    def __init__(self, nums: list):
        self.freqs = Counter(nums)
        self.unique_queue = deque()
        
        for num in nums:
            if self.freqs[num] == 1:
                self.unique_queue.append(num) # remeber "append" not "add"
                
    def showFirstUnique(self) -> int:
        
        while self.unique_queue and self.freqs[self.unique_queue[0]] > 1: # [R] Q can be indexed
            self.unique_queue.popleft()
        
        return -1 if len(self.unique_queue)==0 else self.unique_queue[0]

    def add(self, value: int) -> None:
        if value not in self.freqs:
            self.unique_queue.append(value)
        
        self.freqs[value] += 1
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)