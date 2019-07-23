# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:44:31 2019

@author: Zzj
"""

# 36.二叉搜索树与双向链表 —— 输入一个二叉搜索树，将二叉搜索树转换成一个排序的双向链表，
#                          要求不能创造任何新的节点，只能调整树中节点指针的指向

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution1:
    def Convert(self, pRoot):
        if not pRoot:
            return 
        self.result = []
        self.inOrder(pRoot)
        for i, j in enumerate(self.result[:-1]):
            self.result[i].right = self.result[i+1]
            self.result[i+1].left = j
        
        return self.result[0]
    
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        self.result.append(root)
        self.inOrder(root.right)
        
    
'''class Solution2:
    def Convert(self, pRoot):
        if not pRoot:
            return
        root = pRoot
        pHead = pRoot
        while pHead.left:
            pHead = pHead.left
        self.Core(root)
        return pHead
    
    def Core(self, root):
        if not root.left and not root.right:
            return
        if root.left:
            preRoot = root.left
            self.Core(root.left)
            while preRoot.right:
                preRoot = preRoot.right
            preRoot.right = root
            root.left = preRoot
        if root.right:
            nextRoot = root.right
            self.Core(root.right)
            while nextRoot.left:
                nextRoot = nextRoot.left
            nextRoot.left = root
            root.right = nextRoot
'''
      
if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(12)
    node4 = TreeNode(16)
    node5 = TreeNode(6, left=node1, right=node2)
    node6 = TreeNode(14, left=node3, right=node4)
    pRoot = TreeNode(10, left=node5, right=node6)
    
    a = Solution1()
#    b = Solution2()
    
    pHead1 = a.Convert(pRoot)
    pHead2 = b.Convert(pRoot)
    
    result1 = []
#    result2 = []
    for i in range(7):
        result1.append(pHead1.val)
        pHead1 = pHead1.right
        
#        result2.append(pHead2.val)
#        pHead2 = pHead2.right
        
    print (result1)#, result2)
    
    
    

