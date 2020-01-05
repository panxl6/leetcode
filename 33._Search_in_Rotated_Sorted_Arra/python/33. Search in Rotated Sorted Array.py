# author: 潘兴龙
# date: 2019-06-29 09:58
# coding=utf8

"""
1)  题型剖析：

2)  解法：
二分查找为载体的变种。分类讨论的细节要注意。

3)  知识点讲解: 

4)  follow up：

5)  时间复杂度分析：

6)  备注:

7)  评测结果分析：
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            # 找到了
            if target == nums[mid]:
                return mid
            
            # 常规的二分查找
            if nums[start] <= nums[mid]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                    continue
            else:
                # 找不到
                if target >= nums[start] or target < nums[mid]:
                    end = mid - 1
                    continue
                    
            start = mid + 1
                    
        return -1
