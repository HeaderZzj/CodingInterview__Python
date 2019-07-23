# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:54:07 2019

@author: Zzj
"""

class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeOrderPrint(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def preOrder(self,TreeNode):
        if TreeNode == None:
            return
        # 先打印根结点，再打印左结点，后打印右结点
        print(TreeNode.val)
        self.preOrder(TreeNode.left)
        self.preOrder(TreeNode.right)

    def inOrder(self,TreeNode):
        if TreeNode == None:
            return
        # 先打印左结点，再打印根结点，后打印右结点
        self.inOrder(TreeNode.left)
        print(TreeNode.val)
        self.inOrder(TreeNode.right)

    def postOrder(self,TreeNode):
        if TreeNode == None:
            return
        # 先打印左结点，再打印右结点，后打印根结点
        self.postOrder(TreeNode.left)
        self.postOrder(TreeNode.right)
        print(TreeNode.val)