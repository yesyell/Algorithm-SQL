select category, 
    sum(sales) as total_sales
from book as t1
join book_sales as t2
on t1.book_id = t2.book_id
where sales_date like '2022-01%'
group by category
order by category;