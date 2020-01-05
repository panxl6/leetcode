# author: 潘兴龙
# date: 2019-06-23 13:50
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        return self.__merge(intervals)
    
    def __merge(self, intervals):
        
        interval_len = len(intervals)
        if interval_len <= 1:
            return intervals
        
        # 先排序
        new_intervals = []
        has_overlap = False
        index = 0
        
        while index < interval_len:
            if index == interval_len - 1:
                new_intervals.append(intervals[index])
                break
                    
            if (intervals[index][1] >= intervals[index+1][0] and intervals[index][1] <= intervals[index+1][1]) or (intervals[index+1][1] >= intervals[index][0] and intervals[index + 1][1] <= intervals[index][1]):
                
                left = min(intervals[index][0], intervals[index+1][0])
                right = max(intervals[index][1], intervals[index+1][1])
                
                new_intervals.append([left, right])
                index += 2
                has_overlap = True
            else:
                new_intervals.append(intervals[index])
                
                index += 1
        
        if has_overlap:
            return self.__merge(new_intervals)
        
        return new_intervals
