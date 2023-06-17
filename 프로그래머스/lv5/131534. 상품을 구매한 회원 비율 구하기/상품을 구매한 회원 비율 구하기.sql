select 
    extract(year from sales_date) year, 
    extract(month from sales_date) month, 
    count(distinct u.user_id) puchased_users,
    round((count(distinct u.user_id)/
           (select count(distinct user_id)
            from user_info
            where joined like '2021%')), 1) puchased_ratio
from user_info u
join online_sale s
on u.user_id = s.user_id
where joined like '2021%'
group by 1, 2
order by 1, 2