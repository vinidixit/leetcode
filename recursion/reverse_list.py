#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:37:54 2020

@author: vdixit
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList_recursive(self, cur):
        if cur == None or cur.next == None:
            return cur
        
        print('**1**', cur.val, cur.next.val)
        
        rest = self.reverseList_recursive(cur.next)
        print('**2**', cur.val, cur.next.val, cur.next.next)
        
        cur.next.next = cur
        print('setting None next to:', cur.val) # work in pairs: second master, first sacrificer (sets next to None)
                                                # then in next call sacrificer becomes master. In the end, first el of list will "ultimate" sacrificer
        cur.next = None
        
        return rest
    
    def reverseList_iterative(self, node):
        prev = None
        cur = node
        
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        
        return prev
        
    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        print()
        
    def reverseList(self, head: ListNode) -> ListNode:
        #return self.reverseList_iterative(head)
        head = self.reverseList_recursive(head)
        self.print_list(head)
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)

Solution().print_list(head)
Solution().reverseList(head)
        