## -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 19. 正则表达式的匹配

class Solution:
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        
        # 当模式中第一个字符是*时
        if len(pattern) > 1 and pattern[1] == "*":
            #如果字符串第一个字符与模式第一个字符匹配（相等或者匹配到"."）可以有3种匹配方式：
            if len(s) > 0 and (s[0]==pattern[0] or pattern[0]=="."):
                # 1.模式后移2位字符， 相当于X*被忽略
                # 2.字符串后移1字符， 模式后移两字符
                # 3.字符串后移1字符，模式不变（*可匹配多位）
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:])\
            or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
            
        # 当模式中第二个字符不是*时， 1.如果第一个字符匹配（相等或者为“.”），那么都后移一位，不匹配则返回False
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == "."):
            return self.match(s[1:], pattern[1:])
        return False
    
if __name__ == "__main__":
    a = Solution()
    s = "aaa"
    pattern = "ab*ac*a"
    print(a.match(s, pattern))