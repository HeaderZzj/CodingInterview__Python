# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:28:12 2019

@author: Zzj
"""

# 15.二进制中1的个数

class Solution:
    def Number1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while (n):
            n = (n - 1) & n
            count += 1
        return count
    
    def NumberOf1(self, n):
        return bin(n & 0xffffffff).count("1")
    

if __name__ == "__main__":
    a = Solution()
    print(a.Number1(127))
    print(a.NumberOf1(127))