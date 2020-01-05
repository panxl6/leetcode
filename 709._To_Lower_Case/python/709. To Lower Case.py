# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：典型的操作实现题

2)  解法：遇到大写的字母就转换

3)  知识点讲解: 矩阵的操作还有很多，旋转等。

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

6)  备注:
这一类的题目经常出现在手写bug free的代码面试题中。
a. 遗漏了非字母的判断；
b. 记不清是加32，还是减32；

7)  评测结果分析：
"""

class Solution:
    
    def toLowerCase(self, str: str) -> str:
        
        diff = ord('a') - ord('A')
        
        result = []
        for char in str:
            if not self.isAlpha(char):
                result.append(char)
                continue
                
            if char > 'Z':
                result.append(char)
            else:
                result.append(chr(ord(char) + diff))
        
        return ''.join(result)
    
    def isAlpha(self, char) -> bool:
        
        if char >= 'a' and char <= 'z':
            return True
        
        if char >= 'A' and char <= 'Z':
            return True
        
        return False
