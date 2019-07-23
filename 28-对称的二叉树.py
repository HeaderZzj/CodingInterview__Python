# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:00:56 2019

@author: Zzj
"""

# 28.对称的二叉树

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalCore(pRoot, pRoot)
    
    def isSymmetricalCore(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCore(pRoot1.left, pRoot2.right)\
    and self.isSymmetricalCore(pRoot1.right, pRoot2.left)
        
    
if __name__ == "__main__":

    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(6)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(7)
    node7 = TreeNode(5)

    node1.left,node1.right = node2,node3
    node2.left,node2.right = node4,node5
    node3.left,node3.right = node6,node7
    a = Solution()
    print(a.isSymmetrical(node1))
