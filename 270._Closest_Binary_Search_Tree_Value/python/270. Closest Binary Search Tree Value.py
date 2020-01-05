# author: 潘兴龙
# date: 2019-06-15 16:35
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
二分查找（快速排序过程）跟二叉树是等价的。

4)  follow up：

5)  时间复杂度分析：时间复杂度为o(n*m)

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
    
    result = None
    min_dest = None
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.binarySearch(root, target)
        
        return self.result
    
    def binarySearch(self, root, target):
        
        if root is None:
            return
        
        if self.min_dest is None:
            self.result = root.val
            self.min_dest = abs(root.val - target)
        else:
            new_dest = abs(root.val - target)
            if new_dest < self.min_dest:
                self.min_dest = new_dest
                self.result = root.val
        
        if root.val > target:
            self.binarySearch(root.left, target)
        else:
            self.binarySearch(root.right, target)