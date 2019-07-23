# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:17:18 2019

@author: Zzj
"""

#先定一个node的类
class Node:                  #value + next
    def __init__ (self, x, next=None):
        self.val =  x
        self.next = next

    def getValue(self):
        return self.val

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.val = new_value

    def setNext(self,new_next):
        self.next = new_next

#实现Linked List及其各类操作方法
class LinkedList:
    def __init__(self):      #初始化链表为空表
        self.head = Node(-1) 
        self.tail = None
        self.length = 0
        self.head = self.head.next

    #检测是否为空
    def isEmpty(self):
        return self.head == None  
    
    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self.head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #add在链表前端添加元素:O(1)
    def add(self,value):
        newnode = Node(value,None)    #create一个node（为了插进一个链表）
        newnode.setNext(self.head)   
        self.head = newnode

    #append在链表尾部添加元素:O(n)
    def append(self,value):
        newnode = Node(value)
        if self.isEmpty():
            self.head = newnode   #若为空表，将添加的元素设为第一个元素
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()   #遍历链表
            current.setNext(newnode)   #此时current为链表最后的元素

    #find检索元素是否在链表中    
    def find(self,value):
        current=self.head
        foundvalue = False
        while current != None and not foundvalue:
            if current.getValue() == value:
                foundvalue = True
            else:
                current=current.getNext()
        return foundvalue

    #index索引元素在链表中的位置
    def index(self,value):
        current = self.head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue()==value:
                found = True
            else:
                current=current.getNext()
        if found:
            return count
        else:
            raise ValueError ('%s is not in linkedlist'%value)

    #remove删除链表中的某项元素
    def remove(self,value):
        current = self.head
        pre = None
        while current!=None:
            if current.getValue() == value:
                if not pre:
                    self.head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    #insert链表中插入元素
    def insert(self,pos,value):
        if pos <= 1:
            self.add(value)
        elif pos > self.size():
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)