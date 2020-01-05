# author: 潘兴龙
# date: 2019-02-11 08:25

"""
1)  题型剖析：典型的操作实现题

2)  解法：

3)  知识点讲解: 矩阵的操作还有很多，旋转等。

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：内存占用较多。使用新的变量进行复制，而不是原地修改。
"""

class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_dict = {}

        counter = 0
        for item in emails:
            real_email = self.transfer_email(item)
            if real_email in unique_dict:
                continue
            else:
                unique_dict[real_email] = 1
                counter += 1

        print(unique_dict)
        return counter

    def transfer_email(self, email):

        shortest_email = []
        
        is_escape = False
        for i in range(0, len(email)):
            char = email[i]
            if char == '.':
                continue

            if is_escape is True:
                continue

            if char == '+':
                is_escape = True
                continue

            if char == '@':
                shortest_email += email[i:]
                print(i, email[i:],shortest_email)
                break
            
            shortest_email.append(char)

        return ''.join(shortest_email)
