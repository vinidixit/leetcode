#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:44:15 2020

@author: vdixit
"""


class StockSpanner:
    def __init__(self):
        self.stocks = []
    
    # binary search in already sorted array
    def search_pos(self, arr, new_val):
        # no need to traverse the whole array if there is no possible buy option
        if len(arr) == 0 or new_val <= arr[0]:
            print('return 0 for ', new_val, '->', arr)
            return 0
        
        # no need to traverse the whole array if its current maximum
        if len(arr) > 0 and arr[-1] < new_val:
            return len(arr)
        
        l, r = 0, len(arr)-1
        exact_index = None
        left, right = None, None
        
        while l <= r:
            m = l + (r-l)//2
            
            if arr[m] == new_val:
                exact_index = m
                r = m-1
                
            elif new_val < arr[m]:
                right = m
                r = m-1
            else:
                left = m
                l = m+1
        
        if exact_index:
            print('*1* ', new_val, exact_index)
            return exact_index
        
        if left:
            print('*2* ', new_val, left + 1)
            return left + 1
        
        if right:
            print('*3* ', new_val, right)
            return right
        
        return -1 # Error
    
        
    def next(self, price: int) -> int:
        
        pos = self.search_pos(self.stocks, price)
        if pos == -1:
            print('Error at ', price)
            return
        print(self.stocks, price, pos)
        # shift the array to make room for new value
        self.stocks.insert(pos, price)#self.stocks[:pos] + [price] + self.stocks[pos:]
        print('new arr:', self.stocks)
        return pos + 1
    
        """ O(n)
        stock_span = 1
        
        for stock in self.stocks:
            if stock< price:
                stock_span += 1
                
        self.stocks.append(price)
        return stock_span
        """
            
        
["StockSpanner","next","next","next","next","next","next","next"]
inserts = []#[[100],[80],[60],[70],[60],[75],[85]]
s = StockSpanner()

["StockSpanner","next","next","next","next","next"]
inserts = [[29],[91],[62],[76],[51]]

for val in inserts:
    print('insert : ', val[0])
    print(s.next(val[0]), '\n')

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)