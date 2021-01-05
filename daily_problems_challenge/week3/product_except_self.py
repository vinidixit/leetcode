
"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""
class Solution:
    def productExceptSelf(self, nums):
       
        count_zero = nums.count(0)
        if count_zero > 1:
            return [0]*len(nums)
        
        product = 1
        for num in nums:
            if num == 0:
                continue
            product *= num
            
        for i, num in enumerate(nums):
            if num != 0:
                if count_zero == 1:
                    nums[i] = 0
                else:
                    nums[i] = product//num
            else:
                nums[i] = product
        
        return nums
        