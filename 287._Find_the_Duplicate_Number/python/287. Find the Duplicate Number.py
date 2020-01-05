# author: 潘兴龙
# date: 2019-06-15 10:20

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
去重，第一想到的是用集合（哈希实现）。使用集合的缺点是空间复杂度较高，O(n)。
查找是否存在重复，即存在性问题。

序列操作问题，先排序一下，往往能激发很多的思路。因为O(nlogn)的时间复杂度介于O(N)和O(N^2)之间。

有些比较机智的做法，是可以避免排序的，遍历一次（甚至O可以达到(1)）就可以得到答案。

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        nums = sorted(nums)
        
        i, nums_len = 0, len(nums)
        
        while i < nums_len - 1:
            if nums[i] == nums[i + 1]:
                return nums[i]
            
            i += 1
            
        return None
