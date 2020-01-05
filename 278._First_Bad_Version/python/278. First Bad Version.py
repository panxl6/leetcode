# author: 潘兴龙
# date: 2019-06-13 21:17

"""
1)  题型剖析：二分查找的变种

2)  解法：
目标是否命中的判据，变种

3)  知识点讲解: 

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start, end = 0, n
        
        while start <= end:
            mid = (start + end) / 2
            mid = int(mid)
            
            if isBadVersion(mid) == False:
                if mid >= end:
                    return n
                
                if isBadVersion(mid + 1) == True:
                    return mid + 1
                
                start = mid + 1
            else:
                if mid <= start:
                    return 1
                
                if isBadVersion(mid - 1) == False:
                    return mid
                
                end = mid - 1
        
        return n
    
