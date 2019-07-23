# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:16:22 2019

@author: Zzj
"""

# 24.反转链表

from Link_List import LinkedList

class Solution:
    def ReverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead

if __name__ == "__main__":
    alist = LinkedList()
    for i in range(10):
        alist.append(i)
    length = LinkedList.length(alist)
    pHead = alist.head
    a = Solution()
    reversedlisthead = a.ReverseList(pHead)
    print(length)
    for i in range(length):
        print(reversedlisthead.val)
        reversedlisthead = reversedlisthead.next
        