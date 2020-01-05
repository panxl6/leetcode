# author: 潘兴龙
# date: 2019-07-13 14:48
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 

4)  follow up：

5)  时间复杂度分析：

6)  备注:

7)  评测结果分析：
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        last = [1]
        
        for i in range(1, rowIndex+1):
            
            current = []
            
            for j in range(0, i+1):
                if j - 1 < 0:
                    two = 0
                else:
                    two = last[j-1]
                
                if j > i - 1:
                    first = 0
                else:
                    first = last[j]
                current.append(first + two)
                
            last = current
                
        return last
        