# author: 潘兴龙
# date: 2019-06-15 16:35
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
单向数组的二分查找还是比较容易的，这是最典型的情况。
环的二分查找，是一个变种。

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        return self.bruteSearch(letters, target)
        
    def bruteSearch(self, letters, target):
        
        for letter in letters:
            
            if letter > target:
                return letter
            
        return letters[0]
