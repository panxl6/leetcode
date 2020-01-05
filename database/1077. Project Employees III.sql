# author: 潘兴龙
# date: 2019-06-8 15:43


-- 把父查询的字段（变量）当成参数传递给子查询作为条件

select
    t1.project_id, t1.employee_id
from Project t1
inner join Employee on Employee.employee_id=t1.employee_id    

where experience_years=(
    select 
        max(experience_years)
    from Project t2
    inner join Employee on Employee.employee_id=t2.employee_id   
    where t2.project_id=t1.project_id
    group by t2.project_id
) 

group by t1.project_id, t1.employee_id

