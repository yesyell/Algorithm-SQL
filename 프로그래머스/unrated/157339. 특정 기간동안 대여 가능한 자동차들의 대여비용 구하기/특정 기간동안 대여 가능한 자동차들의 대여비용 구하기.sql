select distinct c.CAR_ID, c.CAR_TYPE,
    round(daily_fee * 30 * (100 - discount_rate) / 100) FEE
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
on c.car_id = r.car_id
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
on c.car_type = d.car_type
where c.car_type in ('세단', 'SUV')
and duration_type = '30일 이상'
and daily_fee * 30 * (100 - discount_rate) / 100 >= 500000 
and daily_fee * 30 * (100 - discount_rate) / 100 < 2000000
and c.car_id not in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date(start_date) <= '2022-11-30'
    and date(end_date) >= '2022-11-01')
order by 3 desc, 2 asc, 1 desc;