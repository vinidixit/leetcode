#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:54:27 2020

@author: vdixit
"""


def compare_bits(n, n1, n2):
       flip_count = 0
       for i in range(1,31): ## 10^9 == 2^30 ==> 30 bits number
           bit = n & 1
           bit1 = n1 & 1
           bit2 = n2 & 1
           n >>= 1
           n1 >>= 1
           n2 >>= 1
           if bit ==1:
               if bit1 ==0 and bit2 == 0:
                   flip_count += 1 # atleast one must be set
           else: # both must be reset
               if bit1 == 1:
                   flip_count += 1
               if bit2 == 1:
                   flip_count += 1
        
       return flip_count  
   
    
print(compare_bits(5, 2, 6))