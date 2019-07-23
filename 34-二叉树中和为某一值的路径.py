# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:48:46 2019

@author: Zzj
"""

# 34.二叉树中和为某一值的路径

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    def FindPath(self, root, expectNum):
        if not root:
            return []
        result = []
        
        def FindPathCore(root, path, currentNum):
            currentNum += root.val
            path.append(root)
            flag = (root.left == None and root.right == None)
            if currentNum == expectNum and flag:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)
            if currentNum < expectNum:
                if root.left:
                    FindPathCore(root.left, path, currentNum)
                if root.right:
                    FindPathCore(root.right, path, currentNum)
            path.pop()
        
        FindPathCore(root, [], 0)
        return result

if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(7)
    node3 = TreeNode(5, left=node1, right=node2)
    node4 = TreeNode(12)
    root = TreeNode(10, left=node3, right=node4)
    
    a = Solution()
    print(a.FindPath(root, 22))