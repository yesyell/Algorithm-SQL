select i.rest_id, rest_name, food_type, favorites, address, 
    round(avg(review_score), 2) as score
from rest_info i
join rest_review r
on i.rest_id = r.rest_id
where address like '서울%'
group by 1
order by 6 desc, 4 desc;