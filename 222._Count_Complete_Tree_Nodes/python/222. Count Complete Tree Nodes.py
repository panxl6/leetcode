# author: 潘兴龙
# date: 2019-06-15 10:59
# coding=utf8

"""
1)  题型剖析：

2)  解法：

3)  知识点讲解: 
表面上看是树的递归遍历。但是完全二叉树的定义限制了，树的节点个数由最下面一层决定。
在最下面一层的节点个数，其实是一个数组的二分查找。类比一下跳跃表是如何查找的。

4)  follow up：
根据现有条件(定义)进一步减少冗余。

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
    
    count = 0
    
    def countNodes(self, root: TreeNode) -> int:
        self.dfs(root)
        
        return self.count
    
    def dfs(self, root):
        
        if root is None:
            return
        
        self.count += 1
        
        self.dfs(root.left)
        self.dfs(root.right)
