select t1.flavor
from first_half t1
join july t2
on t1.flavor = t2.flavor
group by t1.flavor
order by sum(t1.total_order + t2.total_order) desc
limit 3;