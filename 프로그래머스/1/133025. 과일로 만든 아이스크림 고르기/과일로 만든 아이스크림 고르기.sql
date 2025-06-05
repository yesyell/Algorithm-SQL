select fh.flavor
from FIRST_HALF fh
join ICECREAM_INFO ii
on fh.flavor = ii.flavor
where total_order > 3000 and ingredient_type = 'fruit_based'
order by total_order desc