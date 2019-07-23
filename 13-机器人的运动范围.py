# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:25:36 2019

@author: Zzj
"""

# 13.机器人的运动范围

class Solution:
    '''
    def moving(self, threshold, rows, cols):
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        markmatrix = [[0 for i in range(rows)]for j in range(cols)]
        count = self.movingCore(threshold, rows, cols, 0, 0, markmatrix)
        return count
    
    def movingCore(self, threshold, rows, cols, row, col, markmatrix):
        value = 0
        if self.check(threshold, rows, cols, row, col, markmatrix):
            value = 1 + self.movingCountCore(threshold, rows, cols, row-1, col, markmatrix)+ \
            self.movingCountCore(threshold, rows, cols, row+1, col, markmatrix) + \
            self.movingCountCore(threshold, rows, cols, row, col-1, markmatrix) + \
            self.movingCountCore(threshold, rows, cols, row, col+1, markmatrix)
        return value
    
    def check(self, threshold, rows, cols, row, col, markmatrix):
        if row > 0 and row < rows and col > 0 and col < cols \
        and self.getDigitNum(row) + self.getDigitNum(col) <= threshold and not markmatrix[row*cols+col]:
            return True
        return False
    
    def getDigitNum(self, n):
        sum_i = 0
        while (n > 0):
            sum_i += n % 10
            n = n // 10
        return sum_i
        '''
    def movingCount(self,threshold,rows,cols):
        if threshold < 0 or rows<= 0 or cols <= 0:
            return 0
        visited = [[0 for i in range(rows)]for j in range(cols)]
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count

    def movingCountCore(self,threshold,rows,cols,i,j,visited):
        count = 0
        if self.check(threshold,rows,cols,i,j,visited):
            a = visited[1][0]
            visited[i][j] = True
            count = 1 + self.movingCountCore(threshold,rows,cols,i-1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i+1,j,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j-1,visited) \
                      + self.movingCountCore(threshold,rows,cols,i,j+1,visited)
        return count

    def check(self, threshold, rows, cols, i, j, visited):
        if 0<=i<rows and 0<=j<cols  and self.getDigitSum(i,j)<= threshold \
                and not visited[i][j]:
            return True
        return False

    def getDigitSum(self,i,j):
        a = 0
        for index in str(i):
            a += int(index)
        for index in str(j):
            a += int(index)
        return a
        
if __name__ == "__main__":
    a = Solution()
    print(a.movingCount(7, 5, 5))