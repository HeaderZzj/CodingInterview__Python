# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:53:55 2019

@author: Zzj
"""

# 43. 1-n整数中1出现的次数

class Solution:
    def NumberOf1Between1AndN(self, n:float):
        # write code here
        if n < 1:
            return 0
        count = float(0)
        base = float(1)
        round_n = n
        while round_n > 0 :
            weight = round_n % 10
            round_n = round_n // 10
            count += round_n * base
            if weight == 1:
                count += (n % base) + 1
            elif weight > 1:
                count += base
            base *= 10
        return count
    
if __name__ == "__main__":
    n = 12345
    a = Solution()
    print(a.NumberOf1Between1AndN(n))