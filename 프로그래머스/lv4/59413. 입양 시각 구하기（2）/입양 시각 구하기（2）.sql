with recursive t1 as (
    select 0 hour
    union all
    select hour+1
    from t1
    where hour < 23
)
select t1.hour, count(animal_id) count
from t1
left join animal_outs t2
on t1.hour = hour(t2.datetime)
group by 1
order by 1