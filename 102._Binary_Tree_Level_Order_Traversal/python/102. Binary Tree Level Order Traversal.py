# author: 潘兴龙
# date: 2019-07-22 19:55
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
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        return self.__levelOrder(root)
    
    def __levelOrder(self, root):
        
        result = []
        
        queue = [root]
                
        while True:
            
            if len(queue) == 0:
                break
            
            temp = []
            cache = []
            for node in queue:
                if node is None:
                    continue
                
                cache.append(node.left)
                cache.append(node.right)
                
                temp.append(node.val)
                
            if len(temp) > 0:
                result.append(temp)
            queue = cache
            
        return result
