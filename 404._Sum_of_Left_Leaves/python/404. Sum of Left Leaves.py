# author: 潘兴龙
# date: 2019-06-30 13:15
# coding=utf8

"""
1)  题型剖析：
知识点考察。基础操作实现题。

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
    
    total = 0
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        self.total = 0    
        self.__sumOfLeftLeaves(root)
        
        return self.total
    
    def __sumOfLeftLeaves(self, root):
        
        if root is None:
            return
        
        # 左叶子节点
        if root.left is not None and root.left.left is None and root.left.right is None:
            self.total += root.left.val
            
        self.__sumOfLeftLeaves(root.left)
        self.__sumOfLeftLeaves(root.right)
