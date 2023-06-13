select extract(hour from DATETIME) as HOUR, count(*) COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR between 9 and 20
order by HOUR;