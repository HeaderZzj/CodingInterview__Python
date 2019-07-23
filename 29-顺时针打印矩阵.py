# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:59:41 2019

@author: Zzj
"""

# 29. 顺时针打印矩阵

class Solution:
    def printMatrix(self, matrix):
        if not matrix or len(matrix) <=0 or len(matrix[0]) <=0:
            return 
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        while (cols > start*2 and rows > start*2):
            self.printMatrixInCircle(matrix, cols, rows, start, res)
            start += 1
        return res
    
    def printMatrixInCircle(self, matrix, cols, rows, start, res):
        endX = cols-1-start
        endY = rows-1-start
        
        # 左→右
        for i in range(start, endX+1):
            res.append(matrix[start][i])
        
        # 上→下
        if start < endY:
            for i in range(start+1, endY+1):
                res.append(matrix[i][endX])
            
        # 右→左
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                res.append(matrix[endY][i])
        
        # 下→上
        if start < endX and start < endY - 1:
            for i in range(endY-1, start, -1):
                res.append(matrix[i][start])
                
                
if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    a = Solution()
    print(a.printMatrix(matrix))