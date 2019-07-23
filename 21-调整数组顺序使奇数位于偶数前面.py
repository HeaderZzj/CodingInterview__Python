# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:58:52 2019

@author: Zzj
"""

# 21.调整数组顺序使奇数位于偶数前面

class Solution:
    def reOrderArray(self, array):
        if array == None or len(array) == 0:
            return
        pBegin = 0
        pEnd = len(array) - 1
        while(pBegin < pEnd):
            while pBegin < pEnd and not self.isEven(array[pBegin]):
                pBegin += 1
            while pBegin < pEnd and self.isEven(array[pEnd]):
                pEnd -= 1
            if pBegin < pEnd:
#                print(pBegin, pEnd)
                tmp = array[pBegin]
                array[pBegin] = array[pEnd]
                array[pEnd] = tmp
        return array
        
    def isEven(self,number):
        return number & 1==0
    
if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5, 6, 7, 8]
    a = Solution()
    print(a.reOrderArray(alist))
#    print(1&1, 2&1, 3&1, 4&1, 5&1, 6&1, 7&1, 8&1)