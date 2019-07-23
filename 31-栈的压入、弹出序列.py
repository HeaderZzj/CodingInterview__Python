# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:13:12 2019

@author: Zzj
"""

# 31. 栈的压入、弹出序列（根据压栈序列判断另一个序列是否能为此栈的出栈序列）

class Solution:
    def IsPopOrder(self, pushlist, poplist):
        stack = []
        while poplist:
            if pushlist and pushlist[-1] == poplist[0]:
                pushlist.pop()
                poplist.pop(0)
            elif stack and stack[-1] == poplist[0]:
                stack.pop()
                poplist.pop(0)
            elif pushlist:
                stack.append(pushlist.pop())
            else:
                return False
        return True
    

if __name__ == "__main__":
    pushstack = [1, 2, 3, 4, 5]
    popstack1 = [4, 5, 3, 2, 1]
    popstack2 = [4, 3, 5, 1, 2]
    
    a = Solution()
    print(a.IsPopOrder(pushstack, popstack1))
    print(a.IsPopOrder(pushstack, popstack2))