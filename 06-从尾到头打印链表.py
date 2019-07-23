# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:36:23 2019

@author: Zzj
"""

# 6.从尾到头打印链表

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
    def PrintListFromTailToHead(self, listNode):
        if not listNode:
            return []
        res = []
        while listNode.next is not None:
            res.append(listNode.val)
            listNode = listNode.next
        res.append(listNode.val)
        return res[: : -1]

if __name__ == "__main__":
    l = LinkList([1,2,3,4,5])
    l.transform()
    print(Solution().PrintListFromTailToHead(l.head))
'''    l = LinkList([1, 2, 3])
    l.transform()
    head = l.head
    while head :
        print(head.val)
        head = head.next'''

    