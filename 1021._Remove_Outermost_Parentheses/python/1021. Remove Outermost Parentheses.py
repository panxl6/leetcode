# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：典型的基础知识考察+自定义操作实现

2)  解法：

3)  知识点讲解: 嵌套叠加了两个操作：栈的匹配判断；移除最外层括号

4)  follow up：

5)  时间复杂度分析：O(n)

6)  备注:

7)  评测结果分析：
"""

class Solution:
    
    def removeOuterParentheses(self, S: str) -> str:
        
        result, stack = [], []
        
        start, str_len = 0, len(S)
        
        for index in range(0, str_len):
            if S[index] == '(':
                stack.append(S[index])
                continue
                
            stack.pop()
            
            # 是否为一个原始的括号字符串
            if len(stack) != 0:
                continue
                
            # 移除最外层的括号
            result.append(S[start+1 : index])
            start = index + 1
            
        return ''.join(result)