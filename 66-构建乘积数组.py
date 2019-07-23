# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:52:39 2019

@author: Zzj
"""

# 66. 构建乘积数组

class Solution:
    # 给定一个数组 A[0,1,...,n-1] 请构建一个数组B[0,1,...,n-1]
    # 其中B的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
    # 不能使用除法
    def multiply(self, array_A):
        if not array_A:
            return
        C_array = [1]
        for i in range(1, len(array_A)):
            C_array.append(C_array[i-1] * array_A[i-1])
        
        D_array = [1] * len(array_A)
        for i in range(len(array_A)-2, -1, -1):
            D_array[i] = D_array[i+1] * array_A[i+1]
        
        res = []
        
        for i in range(len(array_A)):
            res.append(C_array[i] * D_array[i])
        
        return res
    
if __name__ == "__main__":
    print(Solution().multiply([1, 3, 4, 5, 6, 9, 8, 10]))