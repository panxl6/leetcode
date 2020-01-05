# author: 潘兴龙
# date: 2019-06-8 08:25

"""
1)  题型剖析：典型的操作实现题

2)  解法：

3)  知识点讲解: 矩阵的操作还有很多，旋转等。

4)  follow up：

5)  时间复杂度分析：矩阵遍历，时间复杂度为o(n*m)

6)  备注:

7)  评测结果分析：内存占用较多。使用新的变量进行复制，而不是原地修改。
"""


# Write your MySQL query statement below

select
    project_id, round(sum(Employee.experience_years )/count(project_id), 2) as average_years 
from Project
inner join Employee on Project.employee_id=Employee.employee_id
group by Project.project_id