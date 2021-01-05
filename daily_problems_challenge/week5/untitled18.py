#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:08:41 2020

@author: vdixit
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def isValidSequenceHelper(self, root, arr, cur_ind):
        
        if not root:
            return False # because cur_ind has still not reached end 
        
        if root.val != arr[cur_ind]:
            return False
        
        # check for last node/ must be a leaf : [IMP] Boundary condition
        if cur_ind == len(arr)-1:
            return root.left==None and root.right==None
        
        return self.isValidSequenceHelper(root.left, arr, cur_ind+1) or \
                    self.isValidSequenceHelper(root.right, arr, cur_ind+1)
        
    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        
        return self.isValidSequenceHelper(root, arr, 0)
        