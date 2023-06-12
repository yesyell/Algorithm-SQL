select *
from FOOD_PRODUCT
where PRICE = (
  select max(PRICE)
  from FOOD_PRODUCT
);

select *
from FOOD_PRODUCT
order by PRICE desc
limit 1;