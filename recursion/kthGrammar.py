#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:23:44 2020

@author: vdixit
"""
import math

class Solution:
    
    
    def kthGrammar(self, N: int, K: int) -> int:
        
        # recursive solution
        if N == 1:
            return '0'
        
        row_1_index = math.ceil(K/2)
        row_1_digit = self.kthGrammar(N-1, row_1_index)
        row_digits = '01' if row_1_digit == '0' else '10'
        
        print(N, K, row_1_index, 2*row_1_index, row_digits)
        return row_digits[1] if 2*row_1_index == K else row_digits[0]
        
        
        """ TLE: all digits are independent of each other's computation: So why calculate all!? :)
        digits = []
        for i, dig in enumerate(row):
            digits.append('01' if dig == '0' else '10')
            if 2*(i + 1) >= K:
                break
        """     

print(Solution().kthGrammar(4, 5))