# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:19:46 2019

@author: Zzj
"""

# 17.打印从1到最大的n位数

class Solution:
    def Print1ToMaxNDigits(self, n):
        if n <= 0 :
            return
        
        number = ['0'] * n
        for i in range(10):
            number[0] = str(i)
            self.Print1ToMaxNDigitsRecursively(number, n, 0)
    
    def Print1ToMaxNDigitsRecursively(self, number, length, index):
        if index == length-1:
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index+1] = str(i)
            self.Print1ToMaxNDigitsRecursively(number, length, index+1)
            
    def PrintNumber(self, number):
        isBegining0 = True
        nLength = len(number)
        for i in range(nLength):
            if isBegining0 and number[i] != '0':
                isBegining0 = False
            if not isBegining0:
                print('%c'%number[i])
        print('\t')
        
if __name__ == "__main__":
    a = Solution()
    a.Print1ToMaxNDigits(2)