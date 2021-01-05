#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:02:26 2020

@author: vdixit
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_st = list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.min_st:
            self.min_st.append((x,1))
        else:
            min_el = self.min_st[-1]
            if min_el[0] == x:
                self.min_st.pop()
                self.min_st.append((x, min_el[1]+1))
                
            elif min_el[0] > x:
                self.min_st.append((x,1))
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_st[-1][0]:
            cnt = self.min_st.pop()[1]
            if cnt > 1:
                self.min_st.append((x, cnt-1))

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_st[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()