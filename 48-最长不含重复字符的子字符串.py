# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:52:20 2019

@author: Zzj
"""

# 48. 最长不含重复字符的子字符串

class Solution:
    def lengthOfLongestNoRepeatSubString(self, string):
        if not string or len(string) <= 0:
            return 
        start = 0
        maxLength = 0
        usedchar = {}
        for i in range(len(string)):
            if string[i] in usedchar and start <= usedchar[string[i]]:
                start = usedchar[string[i]] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            usedchar[string[i]] = i
            print(i, start, maxLength, usedchar)
            
        return maxLength
    
if __name__ == "__main__":
    string = "arabcacfr"
    a = Solution()
    print(a.lengthOfLongestNoRepeatSubString(string))