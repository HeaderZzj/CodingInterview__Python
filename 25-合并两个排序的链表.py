# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:47:58 2019

@author: Zzj
"""

# 25.合并两个排序链表
from Link_List import LinkedList

class Solution:
    def merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        MergeHead = LinkedList()
        if (pHead1.val < pHead2.val):
            MergeHead = pHead1
            MergeHead.next = self.merge(pHead1.next, pHead2)
        else:
            MergeHead = pHead2
            MergeHead.next = self.merge(pHead1, pHead2.next)
        return MergeHead
    
if __name__ == "__main__":
    list1 = [1,3,5,6,7]
    list2 = [2,4,8,9]
    chain1 = LinkedList()
    chain2 = LinkedList()
    for i in list1:
        chain1.append(i)
    for i in list2:
        chain2.append(i)
    pHead1 = chain1.head
    pHead2 = chain2.head
    a = Solution()
    MergeHead = a.merge(pHead1, pHead2)
    while MergeHead:
        print(MergeHead.val)
        MergeHead = MergeHead.next
        