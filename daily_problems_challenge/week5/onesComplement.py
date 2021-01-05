#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:28:24 2020

@author: vdixit
"""
import math

class Solution:
    
    def get_msb(self, num):
        pos = 0
        while num:
            num >>= 1
            pos += 1
        return pos
    
    def get_set_num(self, num, pos):
        set_num = 0
        
        for i in range(pos):
            set_num += 1<<i
        
        return set_num
    
    # GeeksForGeeks code
    def onesComplement(self, n): 
        no_of_bits = int(math.log(n)/math.log(2)) + 1  # for 1, 1 is returned
        
        set_num = (1<<no_of_bits) - 1  ## IMP: '-' has more precedance over <<
        
        return n ^ set_num
        

    def findComplement(self, num: int) -> int:
        """ ACCEPTED
        pos = self.get_msb(num)
        set_num = self.get_set_num(num, pos)
        return num ^ set_num
        """
        ## Bit logic
        return self.onesComplement(num)
    
        