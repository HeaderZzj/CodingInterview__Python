# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:13:14 2019

@author: Zzj
"""

# 59. 队列的最大值

class Solution1:
    # 滑动窗口的最大值 给定一个数组和滑动窗口的大小， 找出所有滑动窗口的最大值
    def MaxNumInWindows(self, num, size):
        if not num or size <= 0:
            return []
        res = []
        if len(num) >= size and size >= 1:
            deque = []
            for i in range(size):
                while deque and num[i] >= num[deque[-1]]:
                    deque.pop()
                deque.append(i)
#                print(deque)
            for i in range(size, len(num)):
                res.append(num[deque[0]])
#                print("res=",res)
                while deque and num[i] >= num[deque[-1]]:
                    deque.pop()
                if deque and deque[0] <= i - size:
                    deque.pop(0)
                deque.append(i)
#                print(deque)
            res.append(num[deque[0]])
            
        return res
    
class Solution2:
    # 队列的最大值
    # 实现max，push，pop函数，时间复杂度为O(1)
    def __init__(self):
        self.data = []
        self.max_data = []

    def pop(self):
        if not self.data:
            raise Exception('Empty Queue Cannot Pop')
        if self.data[0] == self.max_data[0]:
            self.max_data.pop(0)
        return self.data.pop(0)

    def push(self, x):
        self.data.append(x)
        while self.max_data and self.max_data[-1] < x:
            self.max_data.pop()
        self.max_data.append(x)

    def max(self):
        return self.max_data[0]
    

    
if __name__ == "__main__":
    alist = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3
    print(Solution1().MaxNumInWindows(alist, size))