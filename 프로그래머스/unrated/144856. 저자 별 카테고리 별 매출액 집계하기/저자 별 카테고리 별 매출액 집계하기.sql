select b.author_id, author_name, category,
    sum(price * sales) total_sales
from book b
join author a
on  b.author_id = a.author_id
join book_sales s
on  b.book_id = s.book_id
where sales_date like '2022-01%'
group by 1, 3
order by 1 asc, 3 desc