# author: 潘兴龙
# date: 2019-07-14 20:47
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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        return self.__search(matrix, target)
    
    def __search(self, matrix, target):
        
        for i in range(0, len(matrix)):
            if matrix[i][0]> target or matrix[i][-1]< target:
                    continue
                    
            for j in range(0, len(matrix[0])):
                                
                if matrix[i][j] == target:
                    return True
                
                if matrix[i][j] > target:
                    break
                
        return False

