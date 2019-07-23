# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:56:04 2019

@author: Zzj
"""

# 30.包含min函数的栈(时间复杂度均为O(1))

class Solution:
    def __init__(self, stack = [], min_stack = []):
        self.stack = stack
        self.min_stack = min_stack
        
    def push(self, node):
        self.stack.append(node)
        if self.min_stack == [] or node < self.minimun():
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.minimun())
        
    def pop(self, node):
        if self.stack == [] or self.min_stack ==[]:
            return None
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def minimun(self):
        return self.min_stack[-1]
        
if __name__ == "__main__":
    stack , min_stack = [], []
    a = Solution(stack, min_stack)
    for i in range(9):
        a.push(i)
        min_num = a.minimun()
    print(stack, min_stack, min_num)