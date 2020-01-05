# author: 潘兴龙
# date: 2019-07-06 21:21
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

import queue

class RecentCounter:

    def __init__(self):
        self.history = []
        self.count, self.head, self.tail = 0, 0, 0
        

    def ping(self, t: int) -> int:
        
        self.history.append(t)
        
        self.count += 1
        self.tail += 1
        
        while self.head < self.tail:
            
            if t - self.history[self.head] > 3000:
                self.count -= 1
                self.head += 1
            else:
                break
        
        return self.count 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)