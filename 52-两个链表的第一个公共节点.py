# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:44:06 2019

@author: Zzj
"""

# 52. 两个链表的第一个公共节点

class Node:                  #value + next
    def __init__ (self, x, next=None):
        self.val =  x
        self.next = next
        
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)
        if length1 > length2:
            longHead = pHead1
            shortHead = pHead2
        else:
            longHead = pHead2
            shortHead = pHead1
        diff = abs(length1 - length2)
        
        for i in range(diff):
            longHead = longHead.next
            
        while longHead != None and shortHead != None and longHead != shortHead:
            longHead = longHead.next
            shortHead = shortHead.next
            
        return longHead
    
    def GetLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1
        return length
    
if __name__ == "__main__":
    node7 = Node(7)
    node6 = Node(6)
    node5 = Node(5, next=node6)
    node4 = Node(4, next=node5)
    node3 = Node(3, next=node6)
    node2 = Node(2, next=node3)
    node1 = Node(1, next=node2)
    
    a = Solution()
    print(a.FindFirstCommonNode(node1, node4).val)
    