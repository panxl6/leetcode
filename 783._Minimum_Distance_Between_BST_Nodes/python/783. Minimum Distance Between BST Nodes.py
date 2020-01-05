# author: 潘兴龙
# date: 2019-06-29 09:58
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
    
    def minDiffInBST(self, root: TreeNode) -> int:
        
        self.result = []
        
        self.__traverse(root)
        self.result = sorted(self.result)
        
        diff = self.result[1] - self.result[0]
        
        for i in range(2, len(self.result)):
            
            diff = min(diff, (self.result[i] - self.result[i - 1]))
        
        return diff
    
    def __traverse(self, root):
        
        if root is None:
            return
        
        self.result.append(root.val)
        
        self.__traverse(root.left)
        self.__traverse(root.right)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    result = []
    
    def minDiffInBST(self, root: TreeNode) -> int:
        
        self.result = []
        
        self.__inorderTraverse(root)
        
        diff = self.result[1] - self.result[0]
        
        for i in range(2, len(self.result)):
            
            diff = min(diff, self.result[i] - self.result[i - 1])
        
        return diff
    
    def __inorderTraverse(self, root):
        
        if root is None:
            return
        
        self.__inorderTraverse(root.left)
        
        self.result.append(root.val)
        
        self.__inorderTraverse(root.right)