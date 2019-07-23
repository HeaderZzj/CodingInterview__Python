# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:16:25 2019

@author: Zzj
"""

# 16.数值的整数次方

class Solution:
    def Power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return 0.0
        if exponent >= 0:
            return self.PowerWithUnsignedExponent(base, exponent)
        return 1.0/self.PowerWithUnsignedExponent(base, exponent)
    
    def PowerWithUnsignedExponent(self, base, exponent):
        result = 1.0
        for i in range(exponent):
            result *= base
        return result
    
if __name__ == "__main__":
    a = Solution()
    print(a.Power(0, 1))
        