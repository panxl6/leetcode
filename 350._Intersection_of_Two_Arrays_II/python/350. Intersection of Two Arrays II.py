# author: 潘兴龙
# date: 2019-06-15 10:06
# coding=utf8

"""
1)  题型剖析：双指针

2)  解法：

3)  知识点讲解: 
集合求交集的变形。允许重复的元素。

4)  follow up：
尝试一下不排序的方式

5)  时间复杂度分析：时间复杂度为O(nlogn)

6)  备注:

7)  评测结果分析：
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        interset = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] == nums2[j]:
                interset.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return interset
