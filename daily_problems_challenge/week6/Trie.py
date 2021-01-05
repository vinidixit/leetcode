#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:00:09 2020

@author: vdixit
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char = None
        self.left = None
        self.middle = None
        self.right = None
        self.is_word = False
    
    def insert_helper(self, root, word, level):
        """
        Inserts a word into the trie.
        """
        if len(word) == level:
            return root
        
        if root==None:
            root = Trie()
    
        if root.char == None:
            root.char = word[level]    
        
        if level ==len(word)-1:
            root.is_word = True 

        
        
             
        if root.char and root.char==word[level]:
            root.middle = self.insert_helper(root.middle, word, level+1)
        
        elif root.char and word[level]< root.char:
            root.left = self.insert_helper(root.left, word, level)
        
        else:
            root.right = self.insert_helper(root.right, word, level)
        
        return root
    
    def insert(self, word: str) -> None:
        cur_node = self
        cur_node = self.insert_helper(cur_node, word, 0)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self
        for i in range(len(word)):
            ch = word[i]
            #print('current',cur_node.char, ch)
            while cur_node and cur_node.char and cur_node.char!=ch:
                #print(ch, cur_node.char)
                if ch < cur_node.char:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
            
            if cur_node == None:
                return False
            
            #print(i, cur_node.is_word)
            if i == len(word)-1:
                return cur_node.is_word
            
            cur_node = cur_node.middle
            
     
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self
        for i in range(len(prefix)):
            ch = prefix[i]
            while cur_node and cur_node.char and cur_node.char!=ch:
                if ch < cur_node.char:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
            
            if cur_node == None or cur_node.char==None:
                return False
            
            print(ch, cur_node.char, cur_node.is_word)
            
            cur_node = cur_node.middle
        
        return True

def print_trie(node):
    if node == None or node.char==None:
        return
    
    print(node.char, node.is_word)
    print_trie(node.left)
    print_trie(node.middle)
    print_trie(node.right)
    
# Your Trie object will be instantiated and called as such:
#obj = Trie()
#obj.insert('a')
#print(obj.startsWith('a'))
#print(obj.search('a'))

ops = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
values = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

obj =Trie()
for op,value in zip(ops,values):
    value = value[0]
    print('\n', op, value)
    if op == 'insert':
        obj.insert(value)
        #print_trie(obj)
    elif op == 'search':
        print(obj.search(value))
        pass
    else:
        print(obj.startsWith(value))
        pass

print_trie(obj)    
"""
word = 'apple'
obj = Trie()
obj.insert(word)
obj.insert('app')
obj.insert('pqr')
print(obj.startsWith('appl'))
print('\n\n')
print_trie(obj)

param_2 = obj.search(word)
print(param_2)

word = 'pqr'
print(word, obj.search(word))


#param_3 = obj.startsWith(prefix)
"""

a False
p False
d False
d True
p True
l False
e True
b False
e False
e False
r True
j False
a False
m True
r False
e False
n False
t False
a False
l True

a False
p False
d False
d True
p True
l False
e True
b False
e False
e False
r True
j False
a False
m True
r False
e False
n False
t False
a False
l True