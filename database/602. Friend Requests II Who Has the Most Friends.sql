# author: 潘兴龙
# date: 2019-06-8 16:40


-- 入度+出度

select
    requester_id as id, (count(accepter_id) + 
    (
        IFNULL((select
            count(requester_id)
        from request_accepted t1
        
        where t1.accepter_id=t2.requester_id
        group by accepter_id), 0)
    )
)as num
from request_accepted t2
group by requester_id
order by num desc limit 1;
