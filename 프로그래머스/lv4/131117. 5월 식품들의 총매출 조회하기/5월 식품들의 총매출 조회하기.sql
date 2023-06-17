select p.product_id, product_name, sum(amount * price) total_sales
from food_product p
join food_order o
on p.product_id = o.product_id
where produce_date like '2022-05%'
group by 1
order by 3 desc, 1 asc;