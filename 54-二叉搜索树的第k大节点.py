# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:36:16 2019

@author: Zzj
"""

# 54.二叉搜索树的第K大节点

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        res = []
        
        def inOrder(pRoot):#中序遍历 左子→父→右子
            if not pRoot:
                return []
            inOrder(pRoot.left)
            res.append(pRoot)
            inOrder(pRoot.right)
        
        inOrder(pRoot)
        if len(res) < k:
            return None
        
        return res[k-1]
    
if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(4)
    node3 = TreeNode(6)
    node4 = TreeNode(8)
    node5 = TreeNode(3, left=node1, right=node2)
    node6 = TreeNode(7, left=node3, right=node4)
    root = TreeNode(5, left=node5, right=node6)
    
    print(Solution().KthNode(root, 3).val)
        
        