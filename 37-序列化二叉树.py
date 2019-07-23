# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:37:51 2019

@author: Zzj
"""

# 37.序列化二叉树 （序列化和反序列化）

from BinaryTree import TreeNode, BinaryTreeOrderPrint

class Solution:
    flag = -1
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + \
    ',' + self.Serialize(root.right)
    
    def Deserialize(self, s):
        self.flag += 1
        lis = s.split(',')
        if self.flag >= len(s):
            return None
        
        root = None
        if lis[self.flag] != '#' :
            root = TreeNode(int(lis[self.flag]), left=self.Deserialize(s),\
                            right=self.Deserialize(s))
        return root
    
if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(12)
    node4 = TreeNode(16)
    node5 = TreeNode(6, left=node1, right=node2)
    node6 = TreeNode(14, left=node3, right=node4)
    pRoot = TreeNode(10, left=node5, right=node6)
    
    a = Solution()
    s = a.Serialize(pRoot)
    print(s)
    root = a.Deserialize(s)
    BinaryTreeOrderPrint().inOrder(root)