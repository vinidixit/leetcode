#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:21:22 2020

@author: vdixit
"""


class Solution:
    
    # Get most significant bit
    def get_msb(self, num):
        res = 0
        i = 0
        
        while num:
            if num & 1 == 1:
                res = i
            i += 1
            num >>=1
        
        return res
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        res = 0
        while m and n:
            bit1 = self.get_msb(m)
            bit2 = self.get_msb(n)
            print(bit1, bit2)
            if bit1 == bit2:
                print(2**2)
                res += 2**bit1
                m -= 2**bit1
                n -= 2**bit1
            else:
                break
        
        return res

print(Solution().rangeBitwiseAnd(5, 7))