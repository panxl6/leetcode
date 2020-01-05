# author: 潘兴龙
# date: 2019-06-09 12:14

"""
1)  题型剖析：知识考察

2)  解法：
a. 使用递归进行深度优先遍历；
b. 使用栈进行遍历
不支持指针的语言，传引用或者使用全局变量；使用对象一般具有跟指针等价的效果。

3)  知识点讲解: 

4)  follow up：
根据先序、中序、后序任意两个序列，推断其中一个遍历顺序

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        
        return self._preorder(root, [])
    
    def _preorder(self, root: 'Node', nodeList: []) -> List[int]:
        
        if root is None:
            return nodeList
        
        nodeList.append(root.val)
        
        for child in root.children:
            self._preorder(child, nodeList)
            
        return nodeList