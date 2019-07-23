# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:03:48 2019

@author: Zzj
"""

# 53. 在排序数组中查找数字

# 统计一个数字在排序数组中出现的次数

class Solution1:
    def GetNumberOfK(self, data, k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.GetFirst(data, length, k, 0, length-1)
            last = self.GetLast(data, length, k, 0, length-1)
            if first > -1 and  last > -1:
                number = last - first + 1
        return number
    
    def GetFirst(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle > 0 and data[middle - 1] == k:
                end = middle - 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetFirst(data, length, k, start, end)
    
    def GetLast(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle < end and data[middle+1] == k:
                start = middle + 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetLast(data, length, k, start, end)
      
class Solution2:
    # 0-n-1中缺失的数字 长度为n-1的数组，有0-n-1 n个数字中 每个数字均为唯一
    def GetMissingNum(self, numbers):
        if not numbers:
            return -1
        start = 0
        end = len(numbers) - 1
        while start <= end:
            mid = (start + end) // 2
            if numbers[mid] == mid:
                start = mid + 1
            elif (mid > 0 and numbers[mid-1] == (mid-1)) or mid == 0:
                return mid
            else:
                end = mid - 1
            if start == len(numbers):
                return len(numbers) - 1
        return -1
    
class Solution3:
    # 数组中数值和下标相等的元素(每个元素都是唯一的)
    def GetNumberSameAsIndex(self, numbers):
        if not numbers:
            return -1
        start = 0
        end = len(numbers) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid == numbers[mid]:
                return mid
            elif mid < numbers[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1 
    
if __name__ == "__main__":
    s1 = [1, 2, 3, 3, 3, 3, 4, 5]
    s2 = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    s3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
    s4 = [-3, -1, 1, 3, 5]
    a = Solution1()
    b = Solution2()
    print(a.GetNumberOfK(s1, 3))
    print(b.GetMissingNum(s2))
    print(b.GetMissingNum(s3))
    print(Solution3().GetNumberSameAsIndex(s4))