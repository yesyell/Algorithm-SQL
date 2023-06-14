select product_code, 
    sum(price * sales_amount) as sales
from product as t1
join offline_sale as t2
on t1.product_id = t2.product_id
group by product_code
order by sales desc, product_code asc;