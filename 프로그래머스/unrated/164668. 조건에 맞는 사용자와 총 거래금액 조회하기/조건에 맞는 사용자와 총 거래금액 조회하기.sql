select user_id, nickname, 
    sum(price) total_sales
from used_goods_board b 
join used_goods_user u
on b.writer_id = u.user_id
where status = 'DONE'
group by 1, 2
having total_sales >= 700000
order by 3