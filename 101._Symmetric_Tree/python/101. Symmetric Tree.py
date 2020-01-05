# author: 潘兴龙
# date: 2019-07-22 20:24
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
                
        while True:
            
            if len(queue) == 0:
                break
                
            right, left = 0, len(queue) - 1
            while right < left:
                if queue[right] is None and queue[left] is None:
                    right += 1
                    left -= 1
                    continue
                    
                if queue[right] is not None and queue[left] is not None and (queue[right].val == queue[left].val):
                    right += 1
                    left -= 1
                    continue
                    
                return False
            
            cache = []
            for node in queue:
                if node is None:
                    continue
                
                cache.append(node.left)
                cache.append(node.right)
                
            queue = cache
            
        return True