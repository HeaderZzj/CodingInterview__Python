# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:06:33 2019

@author: Zzj
"""

# 55. 二叉树的深度

from BinaryTree import TreeNode

class Solution1:
    # 输入一棵二叉树的根节点 求该树的深度 从根到叶节点路径最长的为树的深度
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1
    
class Solution2:
    # 平衡二叉树， 输入一棵二叉树的节点，判断该树是不是平衡二叉树。
    # 如果该树中任意节点的左、右子树的深度相差不超过1， 就是平衡二叉树
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1
    
    def IsBalancedTree(self, pRoot):
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        diff = abs(left - right)
        if diff > 1:
            return False
        return self.IsBalancedTree(pRoot.left) and self.IsBalancedTree(pRoot.right)        
    
if __name__ == "__main__":
    node0 = TreeNode(8)
    node1 = TreeNode(7, left=node0)
    node2 = TreeNode(4)
    node3 = TreeNode(5, left=node1)
    node4 = TreeNode(6)
    node5 = TreeNode(2, left=node2, right=node3)
    node6 = TreeNode(3, right=node4)
    root = TreeNode(1, left=node5, right=node6)
    
    print(Solution1().TreeDepth(root))
    print(Solution2().IsBalancedTree(root))