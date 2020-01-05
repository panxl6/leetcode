# author: 潘兴龙
# date: 2019-06-30 13:24
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
    
    result = []
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        self.result = []
        self.__binaryTreePaths(root, [])
        
        return self.result
    
    def __binaryTreePaths(self, root: TreeNode, path=[]) -> List[str]:
        
        if root is None:
            return
        
        path.append(str(root.val))
                
        if root.left is None and root.right is None:
            self.result.append("->".join(path))
            
        self.__binaryTreePaths(root.left, path.copy())
        self.__binaryTreePaths(root.right, path.copy())
