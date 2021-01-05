#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:14:20 2020

@author: vdixit
"""


def canJump(nums: list) -> bool:
    n = len(nums)
    max_so_far = 0
    for i, num in enumerate(nums):
        if num > 0:
            max_so_far = max(max_so_far, i+num)
        else:
            if max_so_far < i or (max_so_far==i and i < n-1):
                return False
    
    return max_so_far >= n-1