# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:58:15 2019

@author: Zzj
"""

# 7.重建二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Sulotion:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        
        root.left = self.reConstructBinaryTree(pre[1:val+1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])
        
        return root
    

if __name__ == '__main__':
    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    root = Sulotion().reConstructBinaryTree(preorder, inorder)
    while root:
        print(root.val)
        root = root.left
        