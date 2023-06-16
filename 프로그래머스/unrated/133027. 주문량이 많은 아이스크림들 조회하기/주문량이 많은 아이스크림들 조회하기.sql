select t1.flavor
from first_half t1
join (
    select f.flavor, sum(f.total_order) + sum(j.total_order) as total
    from first_half f
    join july j
    on f.flavor = j.flavor
    group by f.flavor) t2
on t1.flavor = t2.flavor
order by t2.total desc
limit 3