# Write your MySQL query statement below

select 
    distinct Sales.product_id, total_quantity
from Sales
inner join  
    (select
        product_id, sum(quantity) as total_quantity
    from Sales
    group by product_id) as t 
on t.product_id=Sales.product_id

