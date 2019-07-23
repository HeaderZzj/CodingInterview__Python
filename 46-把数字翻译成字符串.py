# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:04:42 2019

@author: Zzj
"""

# 46.把数字翻译成字符串 (0-a, 1-b...25-z, 12258-bccfi bwfi bczi mcfi mzi)

class Solution:# 从右往左计算
    def getTranslationCount(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number<0:
            return 0
        numberStr=str(number)

        return self.getTranslationCountCore(numberStr)
    
    def getTranslationCountCore(self,numberStr):
        length=len(numberStr)
        counts=[0]*length
        #count=0
        for i in range(length-1,-1,-1):
            count=0
            if i <length-1:
                count+=counts[i+1]
            else:
                count=1
            
            if i<length-1:
                digit1=int(numberStr[i])
                digit2=int(numberStr[i+1])
                converted=digit1*10+digit2
                if converted>=10 and converted<=25:
                    if i<length-2:
                        count+=counts[i+2]
                    else:
                        count+=1
            counts[i]=count
        return counts[0]
    
if __name__ == "__main__":
    a = Solution()
    print(a.getTranslationCount(12258))
            