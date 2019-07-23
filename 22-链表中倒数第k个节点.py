# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:35:21 2019

@author: Zzj
"""

# 22.链表中倒数第k个节点

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class LinkList:
    def __init__(self,List):
        self.List = List
        self.head = ListNode(-1)
    
    def transform(self):
        l = len(self.List)
        if l == 0:
            return None
        tmp = self.head
        for val in self.List:
            node = ListNode(val)
            tmp.next = node
            tmp = node
        self.head = self.head.next
      
class Solution:
    def FindKthToTail(self, phead, k):
        if not phead or k<=0:
            return None
        pAhead = phead
        pBhind = None
        for i in range(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None
        pBhind = phead
        while pAhead.next:
            pAhead = pAhead.next
            pBhind = pBhind.next
        return pBhind.val
    
if __name__ == "__main__":
    alist=LinkList([1,2,3,4,5,6,7,8])
    alist.transform()
    phead = alist.head.next
    print(phead.val)
    a = Solution()
    print(a.FindKthToTail(phead, k=3))