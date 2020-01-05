# author: 潘兴龙
# date: 2019-07-13 11:33
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
    
    def __init__(self):
        pass
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.__reverse(s, 0, len(s) - 1)
    
    def __reverse(self, s, start, end):
        
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        
        self.__reverse(s, start + 1, end - 1)
        