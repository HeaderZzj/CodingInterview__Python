# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:09:46 2019

@author: Zzj
"""

# 49.丑数（只包含因子2,3,5的数，1为第一个丑数）

class Solution1:#暴力法
    def UglyNumber(self, index):
        if index <= 0:
            return 0
        number = 0
        UglyNumFound = 0
        while (UglyNumFound < index):
            number += 1
            if self.IsUglyNum(number):
                UglyNumFound += 1
        return number
    
    def IsUglyNum(self, number):
        while number % 2 == 0:
            number = number // 2
        while number % 3 == 0:
            number = number // 3
        while number % 5 == 0:
            number = number // 5
        return True if number == 1 else False
    
class Solution2:
    def GetUglyNumber(self, index):
        if index <= 0 :
            return 0
        res = [1]
        nextIndex = 1
        t2 = t3 = t5 = 0
        while nextIndex < index:
            min_val = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(min_val)
            while res[t2]*2 <= min_val:
                t2 += 1
            while res[t3]*3 <= min_val:
                t3 += 1
            while res[t5]*5 <= min_val:
                t5 += 1
            nextIndex += 1
        return res[index-1]
    
if __name__ == "__main__":
    a = Solution1()
    b = Solution2()
    
    print(a.UglyNumber(1500))#暴力法耗时很久
    print(b.GetUglyNumber(1500))
    
    