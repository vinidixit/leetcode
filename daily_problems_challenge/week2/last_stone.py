#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:48:06 2020

@author: vdixit
"""
"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        heapq._heapify_max(stones)
        while len(stones) >= 2:
            max1 = heapq.heappop(stones)
            heapq._heapify_max(stones)
            max2 = heapq.heappop(stones)
            heapq._heapify_max(stones)
            if max1 != max2:
                heapq.heappush(stones, max1-max2)
                heapq._heapify_max(stones)
        
        if stones:
            return heapq.heappop(stones)
        
        return 0