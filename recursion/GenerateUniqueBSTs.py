#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:11:46 2020

@author: vdixit
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def search(self, root, num):
        if root == None:
            return False
        
        if root.val == num:
            return True
        if num < root.val:
            return self.search(root.left, num)
        return self.search(root.right, num)
        
    def insert_bst(self, root, num):
        if root == None:
            return TreeNode(num)
        
        if num < root.val:
            root.left = self.insert_bst(root.left, num)
        else:
            root.right = self.insert_bst(root.right, num)
        
        return root
    
    def remove_bst(self, root, num):
        cur = root
        found = False
        parent_node = None
        
        while not found and cur != None:
            parent_node = cur
            if num < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        if parent_node.left and parent_node.left.val == num:
            parent_node.left = None
        
        if parent_node.right and parent_node.right.val == num:
            parent_node.right = None
        
        return root     
        
    def generateTreesHelper(self, root, n, tree_size, result):
        print(tree_size, root)
        
        if tree_size == n:
            result.append(root)
            print('Returning: ', root.val)
            return root
        
        #for i in range(cur_ind)
        for dig in range(1, n+1):
            if not self.search(root, dig):
                root = self.insert_bst(root, dig)
                print('inserting :', dig, root.val)

                print(root.val, tree_size)
                root = self.generateTreesHelper(root, n, tree_size+1, result)
                root = self.remove_bst(root, dig)
                
        return root       
    
    def generateTrees(self, n: int):
        result = []
        #for r in range(1, n+1):
        #    root = TreeNode(r)
        self.generateTreesHelper(None, n, 0, result)
        return result

Solution().generateTrees(3)