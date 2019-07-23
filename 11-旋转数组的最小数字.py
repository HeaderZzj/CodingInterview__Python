# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:28:21 2019

@author: Zzj
"""

#11.旋转数组的最小数字
class Solution:
    def findmin(self, array_r):
        if not array_r:
            return 
        if len(array_r) == 0:
            return 0
        index1 = 0
        index2 = len(array_r) - 1
        indexMid = index1
        while (array_r[index1]) >= array_r[index2]:
            if (index2 - index1) == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2
            if array_r[index1] == array_r[index2] and array_r[indexMid] >= array_r[index1]:
                return self.minValue(array_r, index1, index2)
            if array_r[indexMid] >= array_r[index1]:
                index1 = indexMid
            if array_r[indexMid] <= array_r[index2]:
                index2 = indexMid
        return array_r[indexMid]
            
    def minValue(self, array_r, index1, index2):
        res = array_r[index1]
        for i in range(index1+1, index2+1):
            if res > array_r[i]:
                res = array_r[i]
        return res
    
if __name__ == "__main__":
    a = Solution()
    array_r = [1, 2, 3, 4, 5]
    print(a.findmin(array_r))
    