select distinct c.CAR_ID, c.CAR_TYPE, 
  round(daily_fee * 30 * (100 - discount_rate) / 100) as FEE
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp
on c.CAR_TYPE = dp.CAR_TYPE
where c.CAR_TYPE in ('세단', 'SUV')
and c.CAR_ID not in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date(END_DATE) >= '2022-11-01' and date(START_DATE) <= '2022-11-30'
)
and dp.DURATION_TYPE = '30일 이상'
having fee >= 500000 and fee < 2000000
order by 3 desc, 2 asc, 1 desc;