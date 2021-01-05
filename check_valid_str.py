#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:44:09 2020

@author: vdixit

Check If Word Is Valid After Substitutions

We are given that the string "abc" is valid.

From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.

If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

"""


def isValid(self, S: str) -> bool:
        # Optimized sol O(N) using stack---- >100ms
        stack = list()
        for ch in S:
            if ch == 'a':
                stack.append(ch)
            elif ch == 'b':
                if len(stack)==0 or stack[-1] != 'a':
                    return False
                
                stack.pop()
                stack.append('ab')
                
            elif ch == 'c':
                if len(stack)==0 or stack[-1] != 'ab':
                    return False
                
                stack.pop() # No need to push abc bcz its == ''
                
            else: # Not present in valid str
                return False
        
        return len(stack)==0
                    
                
        """ -----> 72 ms!
        ## O(N^2) in worst case: N, N-3, N-6... 0 (worst case length of S in each pass)
        while S and 'abc' in S:
            S = S.replace('abc', '')
        
        return len(S)==0
        """