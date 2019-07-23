# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:01:36 2019

@author: Zzj
"""

# 35. 复杂链表的复制（每个节点除了有一个指针指向下一个节点，
#                   还有一个指针指向链表中的任意节点或者None）

class RandomListNode:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random
        
class Solution:
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)
    
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.val = pNode.val
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next
            
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
            
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pNode.next
        pClonedNode = pNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead
    
    def CloneCheat(self, pHead):# 利用python特性
        import copy
        return copy.deepcopy(pHead)
    
    def CloneRecusively(self, pHead):
        if pHead == None:
            return None
        newNode = RandomListNode(pHead.val)
        newNode.random = pHead.random
        newNode.next = self.CloneRecusively(pHead.next)
        return newNode
    
if __name__ == "__main__":
    node1 = RandomListNode(5)
    node2 = RandomListNode(4, node1)
    node3 = RandomListNode(3, node2)
    node4 = RandomListNode(2, node3)
    pHead = RandomListNode(1, node4)
    pHead.random = node3
    node4.random = node1
    node2.random = node4
    
    a = Solution()
    OriginalList = []
    pHeadClone1 = a.Clone(pHead)
    pHeadClone2 = a.CloneCheat(pHead)
    pHeadClone3 = a.CloneRecusively(pHead)
    CloneList1 = []
    CloneList2 = []
    CloneList3 = []
    for i in range(5):
        
        OriginalList.append(pHead.val)
        if pHead.random:
            OriginalList.append(pHead.random.val)
            
        CloneList1.append(pHeadClone1.val)
        if pHeadClone1.random:
            CloneList1.append(pHeadClone1.random.val)
            
        CloneList2.append(pHeadClone2.val)
        if pHeadClone2.random:
            CloneList2.append(pHeadClone2.random.val)
        
        CloneList3.append(pHeadClone3.val)
        if pHeadClone3.random:
            CloneList3.append(pHeadClone3.random.val)
        
        pHead = pHead.next
        pHeadClone1 = pHeadClone1.next
        pHeadClone2 = pHeadClone2.next
        pHeadClone3 = pHeadClone3.next
        
    print(OriginalList, CloneList1, CloneList2, CloneList3, 
          OriginalList == CloneList1,
          OriginalList == CloneList2,
          OriginalList == CloneList3)
    
    
    