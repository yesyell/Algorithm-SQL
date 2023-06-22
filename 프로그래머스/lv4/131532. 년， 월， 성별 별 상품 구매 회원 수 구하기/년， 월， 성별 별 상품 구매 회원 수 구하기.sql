select 
    year(sales_date) year, 
    month(sales_date) month, 
    gender, 
    count(distinct u.user_id) users
from user_info u
join online_sale s
on u.user_id = s.user_id
where gender is not null
group by 1, 2, 3
order by 1, 2, 3;