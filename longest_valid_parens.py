#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:40:06 2020

@author: vdixit
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = list([-1])
        
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    stack.append(-1)
                else:
                    count = 0
                    while stack and stack[-1] not in ['(', -1]:
                        count += stack.pop()
                    
                    if len(stack) == 0 or stack[-1] == -1:
                        if count > 0:
                            stack.append(count)
                        stack.append(-1)
                    else:
                        stack.pop()
                        stack.append(count + 2)
        
        print(stack)
        count = 0
        max_count = 0
        while stack:
            
            if stack[-1] == -1 or stack[-1] == '(':
                max_count = max(max_count, count)
                stack.pop()
                count = 0
            else:
                count += stack.pop()
        
        return max_count
                
                        
                    
print(Solution().longestValidParentheses('(()'))