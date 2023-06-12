select substr(PRODUCT_CODE, 1, 2) as CATEGORY, 
    count(PRODUCT_ID) as PRODUCTS
from product
group by substr(PRODUCT_CODE, 1, 2)
order by PRODUCT_CODE;