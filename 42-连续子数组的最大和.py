# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:29:35 2019

@author: Zzj
"""

# 42. 连续子数组的最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array or len(array) <=0:
            return 0
        
        curNum = 0
        greatNum = float('-inf')
        
        for i in array:
            if curNum <= 0:
                curNum = i
            else:
                curNum += i
            if curNum > greatNum:
                greatNum = curNum
                
        return greatNum
    
if __name__ == "__main__":
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    a = Solution()
    print(a.FindGreatestSumOfSubArray(array))