# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:08:19 2019

@author: Zzj
"""

# 51. 数组中的逆序对 (前一个数字大于后面的数字 如[7,5,6,4]中
#     逆序对为(7,6),(7,5),(7,4),(6,4),(5,4))

class Solution1:
    #巧妙的方法，来源牛客网
    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count%1000000007

class Solution2:    
    #暴力法
    def InversePairs(self, data):
        if len(data) <= 1:
            return 0
        count = 0
        length = len(data)
        for i in range(length-1):
            for j in range(i+1, length):
                if data[i] > data[j]:
                    count += 1
        return count % 1000000007
    
class Solution3:
    #归并排序法
    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        length = len(data)
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        #copy数组为原数组data的复制,在后面充当辅助数组
        count = self.Core(data, copy, 0, length-1)
        return count % 1000000007
    
    def Core(self, data, copy, start,end):
        if start == end:
            copy[start] = data[start]
            return 0

        length = (end-start) // 2 #length为划分后子数组的长度

        left = self.Core(copy, data, start, start+length)
        right = self.Core(copy, data, start+length+1, end)

        #初始化i为前半段最后一个数字的下标
        i = start + length
        #初始化j为后半段最后一个数字的下标
        j = end

        #indexCopy为辅助数组的指针，初始化其指向最后一位
        indexCopy = end
        #准备开始计数
        count = 0
        #对两个数组进行对比取值的操作：
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j-start-length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        
        #剩下一个数组未取完的操作：
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        
        return count+left+right
            
    
if __name__ == "__main__":
    s1 = [7, 5, 6, 4]
    s2 = [7, 5, 6, 4]
    s3 = [7, 5, 6, 4]
    a = Solution1()
    b = Solution2()
    c = Solution3()
    print(a.InversePairs(s1))
    print(b.InversePairs(s2))
    print(c.InversePairs(s3))