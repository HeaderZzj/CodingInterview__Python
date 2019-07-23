# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:16:58 2019

@author: Zzj
"""

# 45.把数组排成最小的数

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        vec = []
        self.Permutation(numbers, 0, vec)
        vec.sort()
        return vec[0]
    
    def Permutation(self, numbers, n, vec):
        if n >= len(numbers):
            vec.append(int(''.join(map(str, numbers))))
        for i in range(n, len(numbers)):
            numbers[i], numbers[n] = numbers[n], numbers[i]
            self.Permutation(numbers, n+1, vec)
            numbers[i], numbers[n] = numbers[n], numbers[i]
            
class Solution2:
    def PrintMinNumber(self, numbers):
        if len(numbers) <= 0:
            return ''
        str_numbers = [str(i) for i in numbers]
        res = sorted(str_numbers)
        return ''.join(res)
    
    
if __name__ == "__main__":
    a = Solution()
    print(a.PrintMinNumber([5, 35, 335, 6, 123, 122, 12]))
    b = Solution2()
    print(b.PrintMinNumber([5, 35, 335, 6, 123, 122, 12]))