#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:53:44 2020

@author: vdixit
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_diameter(self, root, diam):
        if not root:
            return 0
        
        lh = self.get_diameter(root.left, diam)
        rh = self.get_diameter(root.right, diam)
        height = 1 + max(lh, rh)
        
        if lh+rh > diam[0]:
            diam[0] = lh+rh
        
        return height
        
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diam = [0]
        self.get_diameter(root, diam)
        return diam[0]
        