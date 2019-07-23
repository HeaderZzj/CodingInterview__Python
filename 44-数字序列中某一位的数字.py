# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:38:53 2019

@author: Zzj
"""

# 44. 数字序列中某一位的数字(012345678910111213141516171819……)

class Solution:
    def digitAtIndex(self, index):
        if index <= 0:
            return -1
        index = index - 1 #在人看来第一位是0
        digit = 1
        while True:
            numbers = self.countOfIntegers(digit)
            if index < numbers * digit:
                return self.digitAtIndex_2(index, digit)
            index -= digit * numbers
            digit += 1
            
    def countOfIntegers(self, digits):# 得到m位的数字一共多少个，
        #例输入2，返回两位数（10-99）的个数90
        if digits == 1:
            return 10
        count = pow(10, digits-1)
        return 9*count
    
    def digitAtIndex_2(self, index, digit):# 当知道要找的数字位于某m位数之后
        Location = index // digit
        remainder = index % digit
        s = str(self.beginNumber(digit) + Location)
        return s[remainder]
    
    def beginNumber(self, digit):# 求第一个m位数
        if digit == 1:
            return 0
        return pow(10, digit-1)
    
class Solution2:
    def digitAtIndex(self, index):
        if index <= 0:
            return -1
        index = index - 1 #在人看来第一位是0
        s = [i for i in range(index+1)]
        print(s)
        ss = ''.join(map(str, s))
        return ss[index]
        
if __name__ == "__main__":
    a = Solution()
    print(a.digitAtIndex(3))
    b = Solution2()
    print(b.digitAtIndex(3))
    