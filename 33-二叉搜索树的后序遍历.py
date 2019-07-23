# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 09:45:05 2019

@author: Zzj
"""

# 33.二叉搜索树的后序遍历 给出数组判断是否为树的后序遍历

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    def VerifySequenceOfBST(self, sequence):
        if not sequence or len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:#根节点左子树
            if node > root:
                break
            i += 1
        for node in sequence[i:-1]:# 根节点右子树
            if node < root:
                return False
        left = True
        if i >0:
            left = self.VerifySequenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-1:
            right = self.VerifySequenceOfBST(sequence[i: -1])
        return (left and right)
    
if __name__ == "__main__":
    list1 = [5, 7, 6, 9, 11, 10, 8]
    list2 = [7, 4, 5, 6]
    a = Solution()
    print(a.VerifySequenceOfBST(list1))
    print(a.VerifySequenceOfBST(list2))