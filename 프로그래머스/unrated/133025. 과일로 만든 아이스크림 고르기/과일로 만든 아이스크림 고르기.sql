select t1.flavor
from first_half as t1
join icecream_info as t2
on t1.flavor = t2.flavor
where total_order > 3000
and ingredient_type = 'fruit_based'
order by total_order desc;