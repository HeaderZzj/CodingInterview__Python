# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:42:21 2019

@author: Zzj
"""

# 62.圆圈中最后剩下的数字

class Solution:
    # 0~n-1 这n个数字排成一个圆圈， 从数字0开始，每次从圆圈里删除第m个数字。
    # 求剩下的最后一个数字
    def LastRemaining(self, n, m):
        
        #第一个被删除的是(m-1)%n，记该数为k，剩下的为k+1,...,n-1,0,1,...,k-1
        #映射 k+1~0, k+2~1,...,n-1~n-k-2,0~n-k-1,1~n-k,...,k-1~n-2
        #映射前为x，映射后为(x-k-1)%n
        if n < 1 or m < 1:
            return -1
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res
    
if __name__ == "__main__":
    print(Solution().LastRemaining(5, 3))
    