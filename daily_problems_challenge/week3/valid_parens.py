#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:48:47 2020

@author: vdixit
"""
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

"""


## WRONG SOLUTINO
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        l, r, e = 0, 0, 0
        
        for ch in s:
            if ch == '(':
                l += 1
            elif ch == '*':
                e += 1
            else:
                r += 1
                if r > l + e:
                    return False
                
                if r > l and e > 0:
                    rem = r-l
                    while e and rem > 0:
                        rem -= 1
                        e -= 1
                        r -= 1
                
                l -= r
                r = 0
        
        if l == r:
            return True
        
        print(e, l, r)
        if e > 0:
            if abs(l-r) > e:
                return False
            
            return True
        
        return False
        
        
#print(Solution().checkValidString('(*()'))

"""
"(())
((())()()(*)(*()(())())())
()()(
     (()())((()))(*"
                """
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*" 
s = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"
#'((*)'

"""
"((()))
"()(())
"(*()()())**
"(())()()()()
"((*()*))
"(
"(*()*)"
"""
     
valid = True
      
stack = list()
for ch in s:
    if ch in ['(', '*']:
        stack.append(ch)
    else:
        if len(stack) == 0:
            valid = False
            break
        
        if stack[-1] == '(' or len(stack)==1:
            stack.pop()
        else:
            brac_found = False
            e_count = 0
            while stack:
                el = stack.pop()
                if el == '(':
                    brac_found = True
                    break
                else:
                    e_count += 1
                    
            if not brac_found:
                e_count -= 1
                
            while e_count > 0:
                stack.append('*')
                e_count -= 1
                
                
            
        #print(stack)

#print('\n', stack)
e_count = 0
while stack:
    if stack.pop() == '*':
        e_count += 1
    elif e_count == 0:
        valid = False
        break
    else:
        e_count -= 1

print(valid)
            
    