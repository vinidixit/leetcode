#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:31:26 2020

@author: vdixit
"""


class Solution:
    def printReverseString(self, s: list) -> None:
        if s:
            self.printReverseString(s[1:])
            print(s[0])
    
    ## WRONG SOLUTION
    def reverse_string(self, s: list):
        # in place reverse
        
        if len(s) >= 2:
            print('**1**', s)
            self.reverse_string(s[1:-1])  ## a mistake: a new string/list object is getting created
            print('**2**', s)
            s[0], s[-1] = s[-1], s[0]
    
    def reverseStringRecursive(self, s: list, l, r) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if l < r:
            self.reverseStringRecursive(s, l+1, r-1)
            s[l], s[r] = s[r], s[l]
            

s = list('hello')
Solution().reverse_string(s)
print(s)