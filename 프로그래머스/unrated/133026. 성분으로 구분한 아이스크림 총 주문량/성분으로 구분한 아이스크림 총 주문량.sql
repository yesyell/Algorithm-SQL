select ingredient_type, 
    sum(total_order) as total_order
from first_half as t1
join icecream_info as t2
on t1.flavor = t2.flavor
group by ingredient_type
order by total_order;