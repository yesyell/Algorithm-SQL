select distinct c.CAR_ID
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
on c.car_id = r.car_id
where c.car_type = '세단'
and start_date like '%-10-%'
order by 1 desc