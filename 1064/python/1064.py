# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：典型的操作实现题

2)  解法：
凸函数，往右边找；
凹函数，往左边找

3)  知识点讲解: 
待查找的目标为：index == A[index]。由于查找的序列是单调的，相交的点只有一个。

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：内存占用较多。使用新的变量进行复制，而不是原地修改。
"""

class Solution:
    
    NOT_FOUND = -1
    
    def fixedPoint(self, A: List[int]) -> int:
        length = len(A)
        
        if length < 8:
            return self.forceSearch(A, length)
        
        return self.binarySearch(A, 0, length)
    
    # 暴力查找
    def forceSearch(self, A: List[int], arrayLen: int) -> int:
        
        for index in range(0, arrayLen):
            if index == A[index]:
                return index
            
        return self.NOT_FOUND
    
    # 二分查找
    def binarySearch(self, A: List[int], start, end) -> int:
        
        mid = int((start + end)/2)
        
        # 找到了
        if mid == A[mid]:
            return mid
        
        # 已经到达边界了
        if mid == start or mid == end:
            return self.NOT_FOUND
        
        # 向右搜索
        if A[mid] < mid:
            return self.binarySearch(A, mid, end)
        
        # 向左搜索
        return self.binarySearch(A, start, mid)
