"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

-- In the selected subarray, count of zeros and ones should be equal

"""
class Solution:
    
    def findMaxLength(self, nums: list) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -1 if nums[i] == 0 else 1  ## A nice trick: would allow to concatenate multiple valid subarrays to become a bigger valid subarray
            
        max_len = 0
        mappings = dict()
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum == 0:
                max_len = max(max_len, i+1)
            else:
                if cur_sum in mappings:
                    max_len = max(max_len, i-mappings[cur_sum])
            
            if cur_sum not in mappings:
                mappings[cur_sum] = i
        
        return max_len
        
       