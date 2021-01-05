#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:26:16 2020

@author: vdixit
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxPathSumHelper(self, root, max_path_sum):
        if not root:
            return 0
        
        cur_sum = root.val
        
        l_sum = self.maxPathSumHelper(root.left, max_path_sum) # max "branch" sum keeping left node
        r_sum = self.maxPathSumHelper(root.right, max_path_sum) # max "branch" sum keeping right node 
        
        # make a "path" keeping or skipping left and right brances: becuase of "negative" values
        max_path_sum[0] = max(max_path_sum[0], cur_sum, cur_sum + max(l_sum, r_sum, l_sum+r_sum))
                              
        # return max "branch" sum for current node as root:[dont add ls, rs][R]: Not taking a tree 
        return max(cur_sum, cur_sum + max(l_sum, r_sum))
        
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = [root.val] 
        self.maxPathSumHelper(root, max_path_sum)
        return max_path_sum[0]
        