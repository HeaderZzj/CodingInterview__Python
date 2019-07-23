# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:33:51 2019

@author: Zzj
"""

# 14. 剪绳子

class Solution:
    def cutrope(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [0] * (n + 1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        
        for i in range(4, n + 1):
            max_num = 0
            for j in range(1, i//2 + 1):
                product = products[j] * products[i - j]
                if product > max_num:
                    max_num = product
            products[i] = max_num
        return products[n]
    
    def cutrope2(self, n):
        if n < 2: return 0
        if n == 2: return 1
        if n == 3: return 2
        n_3 = 0
        while n >= 5:
            n_3 += 1
            n = n - 3
        return (3 ** n_3) * n
    
if __name__ == "__main__":
    a = Solution()
    print(a.cutrope(9))
    print(a.cutrope2(9))
            