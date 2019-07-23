# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:31:22 2019

@author: Zzj
"""

# 58. 翻转字符串

class Solution1:
    # 输入一个英文句子，翻转句子中单词的顺序， 但单词内字符的顺序不变
    # I am a student. → student a am I
    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while (start < end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
    
    def ReverseSentence(self, s):
        if s == None or len(s) <= 0:
            return ''
        s = list(s)
        s = self.Reverse(s)
        start, end = 0, 0
        res = ''
        temp = []
        while end < len(s):
            if end == len(s) - 1:
                temp.append(self.Reverse(s[start:]))
                break
            if s[start] == ' ':
                start += 1
                end += 1
                temp.append(' ')
            elif s[end] == ' ':
                temp.append(self.Reverse(s[start: end]))
                start = end
            else:
                end += 1
        for i in temp:
            res += ''.join(i)
            
        return res

    def ReverseSentence2(self, s):
        if not s or len(s) <= 0:
            return ''
        s = s.split(' ')
        s = self.Reverse(s)
        res = ''
        for i in s:
            res += ' ' + i
        return res[1:]

class Solution2:
    # 左旋转字符串， 把字符串前面的若干个字符转移到字符串尾部
    # abcdefg num=2 → cdefgab
    def LeftRotateString(self, s, n):
        if not s or len(s) <= 0:
            return ''
        if len(s) <= n:
            return s
        
        s = list(s)
        temp = []
        temp.append(self.Reverse(s[0:n]))
        temp.append(self.Reverse(s[n:]))

#        return ''.join(self.Reverse(sum(temp, [])))
        res = ''
        for i in temp:
            res += ''.join(i)
        return res[::-1]

                
                
    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while (start < end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
    
if __name__ == "__main__":
    s = "I am a student."
    print(Solution1().ReverseSentence(s))
    print(Solution1().ReverseSentence2(s))
    s2 = "abcdefg"
    print(Solution2().LeftRotateString(s2, 2))