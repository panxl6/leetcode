# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：哈希表的常规应用
使用字典进行分类、汇总、统计

2)  解法：

3)  知识点讲解: 矩阵的操作还有很多，旋转等。

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n/2)

6)  备注:
注意统计标记的初始值、初始化；
在白板上写出bug free的代码

7)  评测结果分析：
"""

class Solution:
    
    def repeatedNTimes(self, A: List[int]) -> int:
        
        uniq_dict = {}
        
        for item in A:
            if item in uniq_dict:
                if uniq_dict[item] > 0:
                    return item
                else:
                    uniq_dict[item] += 1
            else:
                uniq_dict[item] = 1
        
        return None
