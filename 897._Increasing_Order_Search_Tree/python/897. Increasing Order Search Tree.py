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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return None
                
        tempNode = self.newRoot = TreeNode(-1)
        
        self.infixOrder(root)
        
        return tempNode.right
    
    def infixOrder(self, root: TreeNode):
        
        if root is None:
            return
        
        self.infixOrder(root.left)
        self.newRoot.right = TreeNode(root.val)
        self.newRoot = self.newRoot.right
        
        self.infixOrder(root.right)
