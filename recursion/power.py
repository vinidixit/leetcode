#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:46:27 2020

@author: vdixit
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        print(n, n//2, int(n/2))
        partial_pow = self.myPow(x, int(n/2))
        
        #print(n, partial_pow)
        
        if n % 2 == 0:
            return partial_pow * partial_pow #1 / (partial_pow * partial_pow) if n < 0 else partial_pow * partial_pow
            
        else:
            return (partial_pow * partial_pow)/x  if n < 0 else x * partial_pow * partial_pow

def power(x, y): 
  
    if(y == 0): return 1
    temp = power(x, int(y / 2))  
      
    if (y % 2 == 0): 
        return temp * temp 
    else: 
        if(y > 0): return x * temp * temp 
        else: return (temp * temp) / x 
        
print(power(34.00515, -3))

print(Solution().myPow(34.00515, -3))

