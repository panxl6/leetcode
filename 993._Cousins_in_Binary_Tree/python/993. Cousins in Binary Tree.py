# author: 潘兴龙
# date: 2019-06-09 13:04

"""
1)  题型剖析：基础知识+自定义概念

2)  解法：

3)  知识点讲解: 
二叉树变换

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
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    
        self.isFound = False
        pathx = self.__traverse(root, x, [])
        
        self.isFound = False
        pathy = self.__traverse(root, y, [])
        
        if len(pathx) != len(pathy):
            return False
        
        if pathx[-2] == pathy[-2]:
            return False
        
        return True
        
    
    def __traverse(self, root, target, path:[]):

        if self.isFound is True:
            return
        
        if root is None:
            return
        
        path.append(root.val)
        if root.val == target:
            self.isFound = True
            return path
        
        ret = self.__traverse(root.left, target, path.copy())        
        if ret is not None:
            return ret
        
        ret = self.__traverse(root.right, target, path.copy())
        if ret is not None:
            return ret
