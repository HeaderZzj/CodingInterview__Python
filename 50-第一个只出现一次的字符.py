# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:52:24 2019

@author: Zzj
"""

# 50. 第一个只出现一次的字符

class Solution:
    def  FirstShowupOnceChar(self, s):
        if len(s) <= 0:
            return -1
        
        char_dict = {}
        for i in s :
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
                
        
        for index, value in enumerate(s):
            if char_dict[value] == 1:
                return s[index]
            
        return -1
    
# 字符流中第一个只出现一次的字符
class Solution2:
    def __init__(self):
        # 引入两个辅助空间：alist数组存储当前读入字符流的字符（按顺序）
        # char_dict存储字符出现的次数。
        self.alist = []
        self.char_dict = {}
    
    def FirstShowupOnce(self):
        while len(self.alist) > 0 and self.char_dict[self.alist[0]] > 1:
            self.alist.pop(0)
        if len(self.alist) > 0:
            return self.alist[0]
        return '#'
        
    def Insert(self, char):
        if char not in self.char_dict.keys():
            self.char_dict[char] = 1
            self.alist.append(char)
        else:
            self.char_dict[char] += 1
    
if __name__ == "__main__":
    s = "abaccdeff"
    a = Solution()
    print(a.FirstShowupOnceChar(s))
    b = Solution2()
    
    