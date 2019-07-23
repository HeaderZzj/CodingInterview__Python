# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:37:30 2019

@author: Zzj
"""

# 27 二叉树的镜像
from BinaryTree import TreeNode, BinaryTreeOrderPrint
        
class Solution:
    def mirror(self, root):
        if not root:
            return 
        if not root.left and not root.right:
            return 
        pTemp = root.left
        root.left = root.right
        root.right = pTemp
        if root.left:
            self.mirror(root.left)
        if root.right:
            self.mirror(root.right)
            
if __name__ == "__main__":
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node5 = TreeNode(2, left=node6, right=node7)
    node4 = TreeNode(9)
    node2 = TreeNode(8, left=node4, right=node5)
    node3 = TreeNode(7)
    node1 = TreeNode(8, left=node2, right=node3)
    
    print(BinaryTreeOrderPrint().preOrder(node1))
    a = Solution()
    a.mirror(node1)
    print(BinaryTreeOrderPrint().preOrder(node1))