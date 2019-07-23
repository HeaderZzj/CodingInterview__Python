# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:55:05 2019

@author: Zzj
"""

# 38.字符串的排列 输入abc 输出所有能排列出来的组合

class Solution:
    def Permutation(self, s):
        if not s:
            return []
        if len(s) == 1:
            return list(s)
        pStr = []
        charlist = list(s)
        charlist.sort()
        
        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i-1]:
                continue
            temp = self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))
            for j in temp:
                pStr.append(charlist[i] + j)
                
        return pStr
    
if __name__ == "__main__":
    s = 'abc'
    a = Solution()
    print(a.Permutation(s))