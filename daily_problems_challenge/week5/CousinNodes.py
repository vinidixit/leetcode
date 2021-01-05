#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:42 2020

@author: vdixit
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int):
        level_nodes = [root]
        found = []
        
        while True:
            next_level = []
            while level_nodes:
                cur_node = level_nodes.pop()
                
                if cur_node.left and cur_node.right:
                    if (cur_node.left.val==x and cur_node.right.val==y) or \
                        (cur_node.left.val==y and cur_node.right.val==x):
                        return False # from same parent
                
                if cur_node.left:
                    next_level.append(cur_node.left)
                    if cur_node.left.val in [x,y]:
                        found.append(cur_node.left.val)
                
                if cur_node.right:
                    next_level.append(cur_node.right)
                    if cur_node.right.val in [x,y]:
                        found.append(cur_node.right.val)
            
            level_nodes = next_level
            
            if len(found) == 2: # node values are unique, it cant be more than 2
                return True
            
            if 2 > len(found) > 0: # nodes are at different levels
                return False
        
        # Didn't find any node in the tree
        return False
            
                
                    
                    
