# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:26:18 2019

@author: Zzj
"""

# 64.求1+2+3+……+n

class Solution:
    # 要求不能使用乘除法 while for if else 等语句和判断句
    def Sum(self, n):
        return self.Sum_Core(n)
    
    def Sum_Core(self, n):
        # 利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况，
        # 如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False。
        func = {False:self.Sum_0, True:self.Sum_Core}
        return n + func[not not n](n-1)
    
    def Sum_0(self, n):
        return 0
    
class Solution2:
    # 利用python特性
    def Sum(self, n):
        return sum(list(range(1, n+1)))
    
class Solution3:
    # 终止递归采用逻辑与的短路特性
    def Sum(self, n):
        return n and n + self.Sum(n-1)
    
if __name__ == "__main__":
    print(Solution().Sum(10))
    print(Solution2().Sum(10))
    print(Solution3().Sum(10))
    
    