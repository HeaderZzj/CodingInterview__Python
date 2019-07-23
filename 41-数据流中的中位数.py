# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:34:25 2019

@author: Zzj
"""

# 41. 数据流的中位数

import heapq

class BigHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return -heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]

class SmallHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]

class Solution:
    def __init__(self):
        self.bigHeap = BigHeap()
        self.smallHeap = SmallHeap()
 
    def addNum(self, num):
        if len(self.bigHeap.arr) == 0:
            self.bigHeap.heap_insert(num)
            return
        if self.bigHeap.get_top() >= num:
            self.bigHeap.heap_insert(num)
        else:
            if len(self.smallHeap.arr) == 0:
                self.smallHeap.heap_insert(num)
                return
            if self.smallHeap.get_top() > num:
                self.bigHeap.heap_insert(num)
            else:
                self.smallHeap.heap_insert(num)
        self.modifyTwoHeapSize()
 
    def getMedian(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize + bigHeapSize == 0:
            return None
        smallHeapHead = self.smallHeap.get_top()
        bigHeapHead = self.bigHeap.get_top()
        if (smallHeapSize + bigHeapSize) %2 == 0:
            return (smallHeapHead+bigHeapHead)/2
        else:
            return smallHeapHead if smallHeapSize > bigHeapSize else bigHeapHead
 
    def modifyTwoHeapSize(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize == bigHeapSize + 2:
            self.bigHeap.heap_insert(self.smallHeap.heap_pop())
        if bigHeapSize == smallHeapSize + 2:
            self.smallHeap.heap_insert(self.bigHeap.heap_pop())


if __name__ == "__main__":
    arr = [68,51,42,92,13,46,24,58,62,72,32]
    a = Solution()
    for i in arr:
        a.addNum(i)
        print(a.getMedian())
        

        
        
    