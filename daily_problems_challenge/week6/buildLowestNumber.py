#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:22:26 2020

@author: vdixit
"""


class Solution:
    def buildLowestNumberRec(self, string, k, res):
     
        if k == 0: 
            res.append(string); 
            return
     
        length = len(string)
  
        if length <= k:
            return
        
        minIndex = 0; 
        for i in range(1, k+1):
            if string[i] < string[minIndex]:
                minIndex = i
        
        if len(res)!=0 or string[minIndex] != '0':
            res.append(string[minIndex])
            
        new_str = string[minIndex+1:]
  
        self.buildLowestNumberRec(new_str, k - minIndex, res) 
    

    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        self.buildLowestNumberRec(num, k, res)
        res_str = ''.join(res) # len(res) = 1 for '' [R]
        
        if len(res_str) == 0:
            return '0'
        
        return res_str

num = '10'
k = 1
print(Solution().removeKdigits(num, k))