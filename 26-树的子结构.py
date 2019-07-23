# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:02:42 2019

@author: Zzj
"""

# 26.树的子结构

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x 
        self.left = left
        self.right = right
        
class Solution:
    def HasSubTree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.SubTreeCore(pRoot1, pRoot2)
            if not res:
                res = self.HasSubTree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubTree(pRoot1.right, pRoot2)
        return res
    
    def SubTreeCore(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        
        return self.SubTreeCore(pRoot1.left, pRoot2.left)\
    and self.SubTreeCore(pRoot1.right, pRoot2.right)
    
if __name__ == "__main__":
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node5 = TreeNode(2, left=node6, right=node7)
    node4 = TreeNode(9)
    node2 = TreeNode(8, left=node4, right=node5)
    node3 = TreeNode(7)
    node1 = TreeNode(8, left=node2, right=node3)

    node9 = TreeNode(9)
    node10 = TreeNode(2)
    node8 = TreeNode(8, left=node9, right=node10)
    
    a = Solution()
    print(a.HasSubTree(node1, node8))
    