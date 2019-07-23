# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 3.数组中重复的数字 
# 题目一 找出数组中重复的数字
class Solution:
    def duplication(self, nums):
        duplication = []
        Hashmap = set()
        for i in range(len(nums)):
            if nums[i] not in Hashmap:
                Hashmap.add(nums[i])
            else:
                duplication.append(nums[i])
        return duplication

    def getDuplication(self, lis):
        #判断边界条件
        if lis == None or len(lis) == 0:
            print('数组为空')
            return False
        # 判断数字在1到n-1的范围内
        Len = len(lis)
        for i in lis:
            if i < 1 or i> Len-1:
                print('值%d不在范围内' % i)
                return False
    
        start,end = 1,Len-1
        while end >= start:
            middle = int(start + 0.5*(end-start))
            count = self.countRange(lis,start,middle)
            #如果只有1个数字时，统计出来的count多于1个，则说明这个数字是重复的
            if end == start:
                if count > 1:
                    return start
                else:
                    print('无重复')
                    break
    
            if count > (middle - start + 1):#若count值大于start到middle的数量，则在其中继续二分查找
                end = middle
            else:
                start = middle + 1
        return False
    
    def countRange(self, lis,start,end):
        count = 0
        for i in lis:
            if i>=start and i<=end:
                count += 1
        return count
if __name__ == "__main__":
    print(Solution().duplication([1, 2, 3, 4, 5, 6, 2, 1, 7]))
    print(Solution().getDuplication([2, 3, 5, 4, 3, 2, 6, 7]))
