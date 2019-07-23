# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:27:21 2019

@author: Zzj
"""

# 5.替换空格 把字符串中每个空格替换成"%20"
class Solution:
    def ReplaceSpace(self, s):
        s = list(s)
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
        p1 = len(s)-1
        s += [None]*(count*2)
        p2 = len(s)-1
        while p1 > 0:
            if s[p1] == ' ':
                for i in ['0', '2', '%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
            
        return ''.join(s)
    
if __name__ == "__main__":
    print(Solution().ReplaceSpace('We are happy'))
            