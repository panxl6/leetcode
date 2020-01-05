# author: 潘兴龙
# date: 2019-07-14 06:44
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
    def findMin(self, nums: List[int]) -> int:
        
        if nums == []:
            return None
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            
            if left == mid:
                mid += 1
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid - 1
                
        
        if left == 0:
            return nums[0]
        
        return None