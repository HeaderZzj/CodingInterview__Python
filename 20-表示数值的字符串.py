# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:16:45 2019

@author: Zzj
"""

# 20. 表示数值的字符串

class Solution:
    def isNumberic(self, s):
        if not s or len(s) <= 0:
            return False
        alist = [i.lower() for i in s]
        if 'e' in alist:
            index = alist.index('e')
            front = alist[:index]
            behind = alist[index+1:]
            if '.' in behind or len(behind) == 0:
                return False
            isfront = self.isDigit(front)
            isbehind = self.isDigit(behind)
            return isfront and isbehind
        else:
            return self.isDigit(alist)
        
    def isDigit(self, alist):
        dotNum = 0
        allow_num = ["0","1","2","3","4","5","6","7","8","9","+","-","."]
        for i in range(len(alist)):
            if alist[i] not in allow_num:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:
                return False
        if dotNum > 1:
            return False
        
        return True
    
if __name__ == "__main__":
    a = Solution()
    a1 = "+100"
    a2 = "5e2"
    a3 = "-123"
    a4 = "-1E-16"
    a5 = "12e"
    a6 = "1a3.14"
    a7 = "1.2.3"
    a8 = "+-5"
    a9 = "12e+5.4"
    print(a.isNumberic(a4))