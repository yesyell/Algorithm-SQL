select ri.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, 
    round(avg(REVIEW_SCORE), 2) as SCORE
from REST_INFO as ri
join REST_REVIEW as rr
on ri.REST_ID = rr.REST_ID
where ADDRESS like '서울%'
group by 1
order by 6 desc, 4 desc;