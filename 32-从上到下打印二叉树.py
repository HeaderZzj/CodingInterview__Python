# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:29:41 2019

@author: Zzj
"""

# 32.从上到下打印二叉树 同一层节点按从左往右打印

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        res_val = []
        res.append(root)
        while len(res) > 0:
            node = res.pop(0)
            res_val.append(node.val)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res_val
    
# 分行从上到下打印二叉树
    def PrintTree(self, pRoot):
        if not pRoot:
            return []
        res = []
        res_val = []
        res.append(pRoot)
        next_Level = 0 # 表示下一层节点数
        toBePrinted = 1 # 表示当前层还未打印的节点数
        temp = []
        while len(res) > 0:
            node = res[0]
            temp.append(node.val)
            if node.left:
                res.append(node.left)
                next_Level += 1
            if node.right:
                res.append(node.right)
                next_Level += 1
            res.pop(0)
            toBePrinted -= 1
            if toBePrinted == 0:
                res_val.append(temp)
                toBePrinted = next_Level
                next_Level = 0
                temp = []
                
        return res_val
    
# 之字形打印二叉树
    def PrintZshape(self, pRoot):
        if not pRoot:
            return []
        res = []
        nodes = [pRoot]
        right = True
        
        while nodes:
            curStack, nextStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            res.append(curStack)
            nextStack.reverse()
            right = not right
            nodes = nextStack
        return res
    
if __name__ == "__main__":
    node1 = TreeNode(11)
    node2 = TreeNode(9)
    node3 = TreeNode(7)
    node4 = TreeNode(5)
    node5 = TreeNode(10, left=node2, right=node1)
    node6 = TreeNode(6, left=node4, right=node3)
    root = TreeNode(8, left=node6, right=node5)
    
    a = Solution()
    print(a.PrintFromTopToBottom(root))
    print(a.PrintTree(root))
    print(a.PrintZshape(root))