with price_rank as (
    select category, price, product_name,
        rank() over (partition by category order by price desc) price_rank
    from food_product
    where category in ('과자', '국', '김치', '식용유')
)
select category, price max_price, product_name
from price_rank
where price_rank = 1
group by 1
order by 2 desc;