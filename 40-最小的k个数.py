# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:27:02 2019

@author: Zzj
"""

# 40. 最小的k个数

class Solution:
    def GetLeastKNums1(self, nums, k):
        # 复杂度O(nlogn)
        if k > len(nums):
            return []
        nums.sort()
        return nums[:k]
    
    def GetLeastKNums2(self, nums, k):
        # 复杂度O(nlogk),用堆的做法
        import heapq
        if k > len(nums):
            return []
        return heapq.nsmallest(k, nums)
    
    def GetLeastKNums3(self, nums, k):
        # 复杂度 O(nlogn)
        if k > len(nums):
            return []
        
        def quicksort(array):
            if not array:
                return []
            pivot = array[0]
            left = quicksort([x for x in array[1:] if x < pivot])
            right = quicksort([x for x in array[1:] if x > pivot])
            return left + [pivot] + right
        return quicksort(nums)[:k]
    
if __name__ == "__main__":
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    
    a = Solution()
    print(a.GetLeastKNums1(nums,k),
          a.GetLeastKNums2(nums,k),
          a.GetLeastKNums3(nums,k))