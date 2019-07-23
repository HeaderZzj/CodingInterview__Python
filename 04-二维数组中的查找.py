# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:05:35 2019

@author: Zzj
"""

# 题目4 二维数组中的查找
class Solution:
    def Find(self, array, target):
        m, n = len(array), len(array[0])
        row = 0
        col = n-1
        while (row < m and col >= 0):
            if array[row][col] > target:
                col -= 1
            elif array[row][col] < target:
                row += 1
            else:
                return True
        return False
    
if __name__ == '__main__':
    array = [[1,2,8,9],
             [2,4,9,12],
             [4,7,10,13],
             [6,8,11,15]]
    target1 = 11
    target2 = 5
    print(Solution().Find(array, target1))
    print(Solution().Find(array, target2))