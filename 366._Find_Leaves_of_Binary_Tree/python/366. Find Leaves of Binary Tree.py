# author: 潘兴龙
# date: 2019-06-09 13:04

"""
1)  题型剖析：知识考察

2)  解法：

3)  知识点讲解: 
a. 二叉树的软删除

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
    
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        result = []
        while True:
            leves = []
            self.__collectLeaves(root, leves)
        
            if len(leves) == 0:
                break
                
            result.append(leves)
        
        return result
    
    def __collectLeaves(self, root, leves:[]):
        
        # 已经被软删除了
        if root.val is None:
            return
        
        # 叶子节点
        if (root.right is None or root.right.val is None) and (root.left is None or root.left.val is None):
            leves.append(root.val)
            
            # 访问过的叶子节点，软删除
            root.val = None
            return
        
        if root.left is not None:
            self.__collectLeaves(root.left, leves)
        
        if root.right is not None:
            self.__collectLeaves(root.right, leves)
