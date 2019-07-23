# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:51:55 2019

@author: Zzj
"""

# 12.矩阵中的路径
class Solution:
    '''
    def way(self, matrix, rows, cols, path):
        if not matrix or rows < 0 or cols <0 or path == None:
            return False
        markmatrix = [0] * (rows * cols)
        pathIndex = 0
        
        for row in range(rows):
            for col in range(cols):
                if self.wayCore(matrix, rows, cols, row, col, path, pathIndex, markmatrix):
                    return True
        return False
    
    def wayCore(self, matrix, rows, cols, row, col, path, pathIndex, markmatrix):
        if pathIndex == len(path):
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and \
        matrix[row*cols + col] == path[pathIndex] and not markmatrix[row*cols + col]:
            pathIndex += 1
            markmatrix[row*cols + col] = True
            haspath = (self.wayCore(matrix, rows, cols, row+1, col, path, pathIndex, markmatrix)\
                       or self.wayCore(matrix, rows, cols, row-1, col, path, pathIndex, markmatrix)\
                       or self.wayCore(matrix, rows, cols, row, col+1, path, pathIndex, markmatrix)\
                       or self.wayCore(matrix, rows, cols, row, col-1, path, pathIndex, markmatrix))
            if not hasPath:
                pathIndex -= 1
                markmatrix[row*cols+col] = False
        return hasPath
        '''
    def hasPath(self, list1, s1):
        if not list1 or not s1:
            return
        rows,cols = len(list1),len(list1[0])
        for i in range(rows):
            for j in range(cols):
                if list1[i][j] == s1[0]:
                    if self.hasPathCore(list1, s1[1:], rows, cols, i, j):
                        return True
        return False

    def hasPathCore(self, list1, s1, rows, cols, i, j):
        if not s1:
            return True
        # lis[i][j] = '*'
        if j + 1 < cols and s1[0] == list1[i][j+1]:#往右找
            return self.hasPathCore(list1, s1[1:], rows, cols, i, j + 1)
        elif j - 1 >= 0 and s1[0] == list1[i][j - 1]:#往左找
            return self.hasPathCore(list1, s1[1:], rows, cols, i, j - 1)
        elif i + 1 < rows and s1[0] == list1[i + 1][j]:#往上找
            return self.hasPathCore(list1, s1[1:], rows, cols, i + 1, j)
        elif i - 1 >= 0 and s1[0] == list1[i - 1][j]:#往下找
            return self.hasPathCore(list1, s1[1:], rows, cols, i - 1, j)
        else:
            return False
    
if __name__ == "__main__":
    list1 = [list('abtg'),
           list('bbbb'),
           list('cfcs'),
           list('jdeh')]
    list2 = [list('abfe'),
            list('abcd'),
            list('adce')]
    s1 = 'bfce'
    s2 = 'bbfe'
    print(Solution().hasPath(list1, s1))