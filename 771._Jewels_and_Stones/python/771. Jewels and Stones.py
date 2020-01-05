# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：典型的操作实现题

2)  解法：
a. 用字典进行分组和统计;
b. 二分查找;

3)  知识点讲解: 一个集合的元素是否在另一个集合中，如果存在，统计出现次数

4)  follow up：

5)  时间复杂度分析：

6)  备注:

7)  评测结果分析：
"""
class Solution:
    
    def numJewelsInStones_v2(self, J: str, S: str) -> int:
        total =0
        
        S, J = sorted(S), sorted(J)
        
        j_len = len(J)
        
        for stone in S:
            if stone > J[-1]:
                continue
                
            if stone < J[0]:
                continue
            
            # 二分查找
            if self.binarySearch(J, stone, 0, j_len) is False:
                continue
                
            total += 1
        
        return total
    
    def binarySearch(self, source, target, start, end):
        mid = int((start + end) / 2)
        
        # 找到目标了
        if target == source[mid]:
            return True
        
        # 到达边界了
        if mid == start or mid == end:
            return False
        
        # 向左搜索
        if target < source[mid]:
            return self.binarySearch(source, target, start, mid)
        
        # 向右搜索
        if target > source[mid]:
            return self.binarySearch(source, target, mid, end)
        
    
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_hash = {}
        for item in J:
            jewel_hash[item] = 0
            
        # 查找
        for stone in S:
            if stone in jewel_hash:
                jewel_hash[stone] += 1
                
        total = 0
        for key, counter in jewel_hash.items():
            total += counter
            
        return total
