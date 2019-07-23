# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:35:48 2019

@author: Zzj
"""

# 61.扑克牌中的顺子

class Solution:
    # 从扑克牌中随机抽5张牌，判断是不是一个顺子 2-10为数字本身
    # A为1， J为11， Q为12， K为13， 大小王可以看成任意数字，定义为0
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()#数组排序
        zeros = numbers.count(0)#统计0的个数
        for i, value in enumerate(numbers[:-1]):
            if value != 0:
                if value == numbers[i+1]:
                    return False
                zeros = zeros - (numbers[i+1] - value - 1)
                #如果空缺的个数小于或者等于0的个数，则为连续的
                if zeros < 0:
                    return False
        return True
    
if __name__ == "__main__":
    a = [0, 1, 3, 4, 5]
    print(Solution().IsContinuous(a))
    