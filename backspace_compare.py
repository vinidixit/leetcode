"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/
"""
class Solution:
    def process_str(self, s):
        i = len(s) -1
        back = 0
        new_s = []
        while i >= 0:
            if s[i] != '#':
                new_s.append(s[i])
                i -= 1
            else:
                while i >= 0 and s[i] == '#':
                    back += 1
                    i -= 1

                while back and i>=0 and s[i] != '#':
                    i -= 1
                    back -=1
                
        return ''.join(new_s)
            
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        return self.process_str(S) == self.process_str(T)