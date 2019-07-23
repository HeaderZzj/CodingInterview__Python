# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:11:42 2019

@author: Zzj
"""

# 57. 和为s的数字

class Solution1:
    # 和为s的两个数字 输入一个排序递增的序列 找出任意两个和为s的数字
    def FindNumsWithSum(self, array, s):
        if not array:
            return []
        left = 0
        right = len(array) - 1
        while left <= right:
            templeft, tempright = array[left], array[right]
            if templeft + tempright == s:
                return [templeft, tempright]
            elif templeft + tempright < s:
                left += 1
            else:
                right -= 1
        return []
    
class Solution2:
    # 和为s的连续正数序列 打印出所有和为s的连续正数序列（至少两个数）
    def FindSequenceWithSum(self, s):
        if s < 3 or not s:
            return []
        small, big = 1, 2
        mid = (1 + s) // 2 # 分界线，超过mid，big+small>s
        curSum = small + big
        res = []
        
        while small < mid:
            if curSum == s:
                res.append(list(range(small, big+1)))
            while curSum > s and small < mid:
                curSum -= small
                small += 1
                if curSum == s:
                    res.append(list(range(small, big+1)))
            big += 1
            curSum += big
        return res
    
if __name__ == "__main__":
    array = [1, 2, 4, 7, 11, 15]
    s = 15
    print(Solution1().FindNumsWithSum(array, s))
    print(Solution2().FindSequenceWithSum(s))
    