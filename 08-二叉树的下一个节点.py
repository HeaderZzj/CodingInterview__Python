# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:13:09 2019

@author: Zzj
"""

class TreeLinkNode:
    def __init__(self, x, left=None, right=None, root=None):
        self.val = x
        self.left = None
        self.right = None
        self.root = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return 
        elif pNode.right != None:#有右子树，下一个节点是右子树的左节点
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        elif pNode.root != None and pNode.root.right == pNode:# 无右子树， 这个节点是父节点的右节点
            while pNode.root != None and pNode.root.left != pNode:
                pNode = pNode.root
            return pNode.root
        else:# 是父节点的左子树 返回父节点
            return pNode.root
    

if __name__ == "__main__":
    n10 = TreeLinkNode('i')
    n9 = TreeLinkNode('h')
    n6 = TreeLinkNode('g')
    n5 = TreeLinkNode('f')
    n4 = TreeLinkNode('e', left=n9, right=n10)
    n3 = TreeLinkNode('d')
    n2 = TreeLinkNode('c', left=n5, right=n6)
    n1 = TreeLinkNode('b', left=n3, right=n4)
    n0 = TreeLinkNode('a', left=n1, right=n2)
    n1.root = n0
    n2.root = n0
    n3.root = n1
    n4.root = n1
    n5.root = n2
    n6.root = n2
    n9.root = n4
    n10.root = n4
    print(Solution().GetNext(n1).val)