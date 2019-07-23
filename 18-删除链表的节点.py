# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:33:56 2019

@author: Zzj
"""

# 18.1 删除链表的节点

class ListNode:
    def __init__(self, x):
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

class Solution1:
    def delete_node(self, List, del_node):
        if not (List.head and del_node):
            return False
        
        if del_node.next:
            del_next_node = del_node.next
            del_node.val = del_next_node.val
            del_node.next = del_next_node.next
            del_next_node.val = None
            del_next_node.next = None
        elif del_node == List.head:
            List.head = None
            del_node = None
        else:
            node = List.head
            while node.next != del_node:
                node = node.next
            node.next = None
            del_node = None
        return List.head
    
# 18.2 删除链表中重复的节点
class Solution2:
    def deleteDuplication(self, List):
        head = List.head
        first = ListNode(-1)
        first.next = head
        last = first
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                last.next = head
            else:
                last = head
                head = head.next
        return first.next
    
    def deleteDuplication2(self, List):
        head = List.head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = list(filter(lambda c: res.count(c) == 1, res))
        new_List = ListNode(0)
        pre = new_List
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return new_List.next
    
if __name__ == "__main__":
    l = LinkList([1,2,3,4,5])
    l.transform()
    head = l.head
    a = Solution1()
    node1 = head.next.next
    a.delete_node(l, node1)
    while head:
        print(head.val)
        head = head.next
        
    l2 = LinkList([1, 2, 3, 4, 5, 5, 6, 6, 6])
#    l2 = LinkList([1, 1, 1, 2, 2, 3])
    l2.transform()
    b = Solution2()
#    b.deleteDuplication(l2)
    b.deleteDuplication2(l2)
    head2 = l2.head
    while head2:
        print(head2.val)
        head2 = head2.next
    