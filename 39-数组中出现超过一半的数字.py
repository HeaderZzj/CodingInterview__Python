# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:04:41 2019

@author: Zzj
"""

# 39.数组中出现次数超过一半的数字

class Solution:#(O(n))
    def MoreThanHalfNum(self, nums):
        if not nums or len(nums) <= 0:
            return 0
        
        res = nums[0]
        times = 1
        
        for i in range(1, len(nums)):#(超过一半的数字出现的次数比其他数字加起来都多)
            if times == 0:
                res = nums[i]
                times = 1
            elif nums[i] == res:
                times += 1
            else:
                times -= 1
                
        def CheckMoreThanHalf(nums, number):
            length = len(nums)
            times = 0
            
            for i in range(length):
                if nums[i] == number:
                    times += 1
                    
            if times*2 <= length:
                return False
            return True
        
        if CheckMoreThanHalf(nums, res):
            return res
        
        return 0
    
    def MoreThanHalfNum_Solution2(self, nums):#简化写法
        if not nums or len(nums) <= 0:
            return 0
        res = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if times == 0:
                res = nums[i]
                times = 1
            elif nums[i] == res:
                times += 1
            else:
                times -= 1
        num_sum = 0
        for j in nums:
            if j == res:
                num_sum += 1
        return res if num_sum*2 > len(nums) else 0
    
if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    a = Solution()
    print(a.MoreThanHalfNum(nums))
    print(a.MoreThanHalfNum_Solution2(nums))
    