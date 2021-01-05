#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:23:49 2020

@author: vdixit

Tricky trick: Kadane subarray sum still takes O(n^2) to search for required subarray. 
So, save sub-array sums in hash instead in an array. 
And, keep saving and searching in same loop, to avoid search in Right sum (might get duplicate 
                                    counts or increase complexity of solution)


"""


import collections

class Solution:
    def subarray_sum_bruteforce(self, arr, k):
        count = 0
        n = len(arr)
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += arr[j]
                if cur_sum == k:
                    count += 1
        
        return count
    
    def subarray_sum_dp(self, arr, k):
        n = len(arr)
        subset_sums = [0]*n
        subset_sums[0] = arr[0]
        for i in range(1, n):
            subset_sums[i] = subset_sums[i-1] + arr[i]
        
        count = 0
        for i in range(n):
            if subset_sums[i] == k:
                count += 1
            for j in range(0, i):
                if subset_sums[i]-subset_sums[j]==k:
                    count += 1
        
        return count
    
    def subarray_sum_hashing(self, arr, k):
        n = len(arr)
        count = 0
        cur_sum = 0
        sub_hash = collections.Counter()
        
        for num in arr:
            cur_sum += num
            if cur_sum == k:
                count += 1
            
            if cur_sum-k in sub_hash:
                count += sub_hash[cur_sum-k]
            
            sub_hash[cur_sum] += 1
        return count
    
                
    def subarraySum(self, nums: List[int], k: int) -> int:
        #return self.subarray_sum_bruteforce(nums, k) # TLE
        #return self.subarray_sum_dp(nums, k) # TLE
        return self.subarray_sum_hashing(nums, k)
        