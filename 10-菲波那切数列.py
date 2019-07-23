# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:48:03 2019

@author: Zzj
"""

# 10.求斐波那切数列的第n项

class Solution:
    def fib_Loop(self, n):# 循环
        small = 0
        big = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            sum_i = small + big
            small = big
            big = sum_i
        return big
    
    def fib_Recursion(self, n):# 递归
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self.fib_Recursion(n-1) + self.fib_Recursion(n-2)
    
    
if __name__ == "__main__":
    print(Solution().fib_Loop(10))
    print('\n')
    print(Solution().fib_Recursion(10))
    
    