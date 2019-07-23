# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:16:46 2019

@author: Zzj
"""

# 63. 股票的最大利润

class Solution:
    # 股票价格按时间先后顺序储存在数组中，求买卖一次的最大利润
    def MaxProfit(self, prices):
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
if __name__ == "__main__":
    prices = [9, 11, 8, 5, 7, 12, 16, 14]
    print(Solution().MaxProfit(prices))