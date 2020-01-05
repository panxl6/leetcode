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

select
    project_id
from (
    select
        project_id, count(employee_id) as total
    from Project
    group by project_id
    order by total desc
) t1
where total =(
	select
	    max(total) as max_total
	from (
	    select
	        project_id, count(employee_id) as total
	    from Project
	    group by project_id
	    order by total desc
	) t 
)
