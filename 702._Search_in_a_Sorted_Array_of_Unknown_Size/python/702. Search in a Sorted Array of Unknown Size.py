# author: 潘兴龙
# date: 2019-06-15 17:11
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
二分查找的基础是建立在待查找的序列已知（静态的）、有序。
但是如果，这个带查找的序列是未知的，就像题中给定的场景。例如：序列太大，无法放入内存；又或者是动态生成的。
TCP拥塞控制的慢启动思路会是个方法。步长递增的探查方式。

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

class Solution:
    
    OUT_OF_BOUND = 2147483647
    
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        return self.dynamicSearch(reader, target)
        
    
    def bruteSearch(self, reader, target):
        
        i = 0
        while True:
            number = reader.get(i)
            
            if number == self.OUT_OF_BOUND:
                return -1
            
            if number == target:
                return i
            elif number > target:
                return -1
            
            i += 1
            
        return -1

    
    # 逐步加大区间，参考TCP拥塞控制机制的慢启动
    def dynamicSearch(self, reader, target):
        
        index, step = 0, 1
        while True:
            
            number = reader.get(index)
            if number == target:
                return index
            elif number > target:
                last_index = index - step
                while last_index < index:
                    number = reader.get(last_index)
                    
                    if number == self.OUT_OF_BOUND:
                        return -1
                    
                    if number == target:
                        return last_index
                    
                    if number > target:
                        return -1
                    
                    last_index += 1
            
            step += 2
            index += step
    