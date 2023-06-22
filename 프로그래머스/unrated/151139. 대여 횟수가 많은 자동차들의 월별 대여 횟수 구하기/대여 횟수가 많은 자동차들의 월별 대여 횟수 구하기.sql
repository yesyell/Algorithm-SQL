select extract(month from START_DATE) MONTH, CAR_ID, count(*) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (
    select distinct CAR_ID 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between '2022-08-01' and '2022-10-31'
    group by CAR_ID
    having count(HISTORY_ID) >= 5) 
and START_DATE between '2022-08-01' and '2022-10-31'
group by 1, 2
order by 1 asc, 2 desc