# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:22:24 2019

@author: Zzj
"""

# 9.用两个栈实现队列-1
# 9.用两个队列实现栈-2

class Solution1:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def pushTail(self, node):
        self.stack1.append(node)
    
    def popTail(self):
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

class Solution2:
    def __init__(self):
        self.query1 = []
        self.query2 = []
        
    def querypush(self, n):
        self.query1.insert(0, n)
        
    def querypop(self):
        if not self.query1:
            return None
        
        while len(self.query1) != 1:
            self.query2.insert(0, self.query1.pop())
        self.query1, self.query2 = self.query2, self.query1
        return self.query2.pop()
        
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(list1)
    a = Solution1()
    b = Solution2()
    for i in list1:
        a.pushTail(i)
        b.querypush(i)
    for i in range(n):
        print(a.popTail())
    for i in range(n):
        print(b.querypop())
        