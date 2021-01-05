#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:28:31 2020

@author: vdixit
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import numpy as np
import copy 

class Solution:
    
    def generateTreesHelper(self, root, l , r, arr, tree_size,n, result):
        
        if l > r:
            return None
        
        for i in range(l, r+1):
            root = TreeNode(arr[i])
            root.left = self.generateTreesHelper(root, l, i-1, arr,tree_size+1,n, result)
            root.right = self.generateTreesHelper(root, i+1, r, arr, tree_size+1,n, result)
            
            if tree_size == n-1:
                print_tree([root])
                print('\n')
                result.append(root)
            
        return root
        
        
    def generateTrees(self, n: int): 
        arr = np.arange(1, n+1)
        result = []
       
        root = self.generateTreesHelper(None, 0, n-1, arr,0, n, result) # [R] boundary case: 1->0 so, n->n-1
        
        return result, root
    
def print_tree(level_nodes):
    next_level = []
    
    for i in range(len(level_nodes)):
        if level_nodes[i] != None:        
            if level_nodes[i].left != None:
                print(level_nodes[i].left.val, end = ' ')
                next_level.append(level_nodes[i].left)
            else:
                print(level_nodes[i].left, end = ' ')
            
            if level_nodes[i].right != None:
                print(level_nodes[i].right.val, end = '| ')
                next_level.append(level_nodes[i].right)
            else:
                print(level_nodes[i].right, end = '| ')
    
    if next_level:
        print_tree(next_level)

r1, r2 = Solution().generateTrees(3)
print(len(r1), r2.val)

print_tree([r2])
print('\n\n')
"""
for t in r1:
    print(t.val)
    print_tree([t])
    print()
    print('--'*20)
"""