#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:16:15 2020

@author: vdixit
"""

"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Solution inspired from Logical reasoning's Direction problem :)
"""
class Solution:
    class Solution:
        def stringShift(self, s: str, shifts: list[list[int]]) -> str:
            n = len(shifts)
            
            for i in range(n):
                shifts[i][0] = -1 if shifts[i][0]==0 else 1
                
            shift_agg = 0
            for shift in shifts:
                shift_agg += shift[0]*shift[1]
                
            if shift_agg == 0:
                return s
            
            sign = -1 if shift_agg < 0 else 1
            shift_agg = sign * abs(shift_agg)%n   ### IMP to avoid cyclic inconsistency
            
            sub1, sub2 = s[:-shift_agg], s[-shift_agg:]
            return sub2 + sub1
            
            
    """
    # Longer COde: DoinG THE SAMETHING
    
    def stringShift(self, s: str, shifts: list[list[int]]) -> str:
        n = len(shifts)
        
        for i in range(n):
            shifts[i][0] = -1 if shifts[i][0]==0 else 1  ## will keep direction in check during ops
            
        shift_agg = shifts[0]
        
        for i in range(1, n):
            shift = shifts[i]
            agg = shift_agg[0]*shift_agg[1] + shift[0]*shift[1]
            
            if agg > 0:
                shift_agg = [1, agg]
            elif agg < 0:
                shift_agg = [-1, -agg]
            else:
                shift_agg = [0,0]
       
        if shift_agg[0] == 0:
            return s
        
        direction, amount = shift_agg
        amount = amount %n
        
        sub1, sub2 = s[:-direction*amount], s[-direction*amount:]
        return sub2 + sub1
     """   
            
            