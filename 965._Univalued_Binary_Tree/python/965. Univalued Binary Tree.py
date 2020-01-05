# author: 潘兴龙
# date: 2019-06-09 12:40

"""
1)  题型剖析：自定义概念

2)  解法：

3)  知识点讲解: 

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

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
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        return self._isUnivalTree(root, root.val)
    
    
    def _isUnivalTree(self, root: TreeNode, target) -> bool:
        
        if root is None:
            return True
        
        if root.val != target:
            return False
            
        return self._isUnivalTree(root.left, target) and self._isUnivalTree(root.right, target)
