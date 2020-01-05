# author: 潘兴龙
# date: 2019-06-29 09:58
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
利用二叉查找树的有序性，进行剪枝，可以减少不必要的搜索。

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
    
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        self.__rangeSum(root, L, R)
        return self.total
    
    def __rangeSum(self, root, L, R):
        
        if root is None:
            return
        
        
        print(root.val)
        
        if root.val >= L and root.val <= R:
            self.total += root.val
        
        if root.val <= R:
            self.__rangeSum(root.right, L, R)
        
        if root.val >= L:
            self.__rangeSum(root.left, L, R)
