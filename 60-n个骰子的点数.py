# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:22:26 2019

@author: Zzj
"""

# 60.n个骰子的点数

class Solution:
    # 所有骰子朝上一面的点数和为s，n个骰子，打印出s的所有可能的值出现的概率
    # 思路是固定第一个骰子，计算后面n-1个骰子出现的次数。递归。
    def __init__(self):
        self.pProbabilities = {}# n个骰子相加之和出现的次数
        self.g_maxVal = 6

    def PrintProbability(self,number):
        if number < 1:
            return
        self.Probability(number)
        total = pow(self.g_maxVal, number)
        for i in self.pProbabilities.items():
            print('%d %.5f' % (i[0], i[1] / total))

    def Probability(self,number):
        for i in range(1, self.g_maxVal + 1):
            # 第一个骰子的值，从1循环到6
            self.Probability2(number, i)

    def Probability2(self,current,tsum):
        if current == 1:
            # 当处理完前面n—1个骰子，剩下1个骰子的时候，次数加一
            self.pProbabilities[tsum] = self.pProbabilities.get(tsum, 0) + 1
        else:
            for i in range(1, self.g_maxVal + 1):
                # 处理后面n-1个骰子
                self.Probability2(current - 1, i + tsum)
                
class Solution2:
    # 循环做法
    def __init__(self):
        self.g_maxValue = 6

    def PrintProbability(self,number):
        if number < 1:
            return
        pProbabilities = [[0] * (self.g_maxValue * number + 1), [0] * (self.g_maxValue * number + 1)]
        flag = 0
        for i in range(1, self.g_maxValue + 1):
            pProbabilities[flag][i] = 1

        # 这里k表示第几个骰子
        for k in range(2, number + 1):
            for i in range(k):
                pProbabilities[1 - flag][i] = 0
            # self.g_maxValue*k表示k个骰子最大点数之和。这里i表示点数之和
            for i in range(k, self.g_maxValue * k + 1):
                pProbabilities[1 - flag][i] = 0
                j = 1
                while j <= i and j <= self.g_maxValue:
                    # 一个数组的第n项等于另一个数组的第n-1，n-2，n-3，n-4，n-5，n-6项之和
                    pProbabilities[1 - flag][i] += pProbabilities[flag][i - j]
                    j += 1
            flag = 1-flag

        total = pow(self.g_maxValue, number)
        for i in range(number,self.g_maxValue*number+1):
            ratio = pProbabilities[flag][i]/total
            print('%d %.5f' % (i, ratio))
                
if __name__ == "__main__":
    print(Solution().PrintProbability(5))
    print(Solution2().PrintProbability(2))