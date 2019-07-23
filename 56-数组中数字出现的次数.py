# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:29:08 2019

@author: Zzj
"""

# 56.数组中数字出现的次数

class Solution1:
    # 数组中只出现一次的两个数字(要求时间复杂度O(n), 空间复杂度o(1))
    
    # 从头到尾依次异或每个数字 最终的结果刚好是只出现一次的数字
    # 将数组分成两个数组 每个数组包含其中一个只出现一次的数字
    # 在结果数字中找到第一个为1的位的位置，记为第n位
    # 将第n位为0的分为一组，为1的分为一组
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return
        result = 0
        for i in array:
            result = result ^ i 
        index = self.FindFirstBit(result)
        res1, res2 = 0, 0
        for i in array:
            if self.isBit(i, index):
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]
    
    def FindFirstBit(self, num):
        # 用于在整数num的二进制表示中找到最右边是1的位
        indexBit = 0
        while (num&1 == 0 and indexBit < 32):
            num = num >> 1
            indexBit += 1
        return indexBit
    
    def isBit(self, num, indexBit):
        # 用于判断在num的二进制表示中从右边起的indexBit位是否为1
        num = num >> indexBit
        return (num & 1)
    
class Solution2:
    # 数组中唯一只出现一次的数据
    def FindNumAppearOnce(self, array):
        if not array:
            return
        
        bitSum = [0] * 32
        for i in array:
            bitMask = 1
            for j in range(31, -1, -1):
                bit = i & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1
        result = 0
        for i in bitSum:
            result = result << 1
            result += i % 3
        
        return result
            
        
if __name__ == "__main__" :
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    print(Solution1().FindNumsAppearOnce(array))
    array2 = [1, 2, 2, 2, 3, 3, 3]
    print(Solution2().FindNumAppearOnce(array2))
    