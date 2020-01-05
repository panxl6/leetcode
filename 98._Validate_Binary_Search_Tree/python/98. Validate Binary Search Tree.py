# author: 潘兴龙
# date: 2019-07-14 20:47
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
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.__isValidBST(root, None, None)
    
    def __isValidBST(self, root: TreeNode, leftLimit, rightLimit) -> bool:
        
        if root is None:
            return True
        
        if root.left is not None:
            if root.left.val >= root.val:
                return False
            
            if leftLimit is not None and root.left.val <= leftLimit:
                return False
            
        if root.right is not None:
            if root.right.val <= root.val:
                return False
            
            if rightLimit is not None and root.right.val >= rightLimit:
                return False
            
        return self.__isValidBST(root.left, leftLimit, root.val) and self.__isValidBST(root.right, root.val, rightLimit)
        
        