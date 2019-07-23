# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:07:47 2019

@author: Zzj
"""

# 47.礼物的最大价值

class Solution:
    #假设输入array为一维数组，行数为rows,列数为cols,要求输出为最大的那个数值
    #利用了一个辅助的二维数组maxValues 有rows行cols列
    def getMaxValue1(self, array, rows, cols):
        if array==[] or rows<=0 or cols<=0:
            return 0
        maxValues=[[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                left=0
                up=0
                if i>0: 
                    #如果行号大于0，说明它上面有数字
                    up=maxValues[i-1][j]
                if j>0:
                    #如果列号大于0，说明它左边有数字
                    left=maxValues[i][j-1]
                maxValues[i][j]=max(up, left)+array[i*cols + j]

        return maxValues[rows-1][cols-1]


    def getMaxValue2(self, array, rows, cols):
        #利用一维数组，有cols列(更节省空间)
        if array == [] or rows <= 0 or cols <= 0:
            return 0
        maxValues=[0 for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                up=0
                left=0
                if i>0:
                    #如果行号大于0，说明它上面有数字。up仍为当前列的maxValue
                    up=maxValues[j]
                if j>0:
                    #如果列号大于0，说明它左边有数字。
                    left=maxValues[j-1]
                maxValues[j]=max(up,left)+array[i*cols+j]
        return maxValues[cols-1]
            
        



if __name__=="__main__":
    a = Solution()
    print(a.getMaxValue1([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4))
    print(a.getMaxValue2([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4))
    