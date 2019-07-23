# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:35:13 2019

@author: Zzj
"""

# 65. 不用加减乘除做加法

class Solution:
    def Add(self, num1, num2):
        while num2:
            Sum = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = Sum
            num2 = carry
        if num1 < 0x7fffffff:
            return num1
        else:
            # ~ 按位取反
            return ~(num1 ^ 0xffffffff)
        
'''
不使用新的变量，交换两个变量的值.
基于加减法    基于异或运算
a = a + b     a = a ^ b
b = a - b     b = a ^ b
a = a - b     a = a ^ b
'''

if __name__ == "__main__":
    print(Solution().Add(100,999))
        