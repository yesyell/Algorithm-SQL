select ANIMAL_TYPE, count(ANIMAL_ID) as count
from ANIMAL_INS
group by ANIMAL_TYPE
having ANIMAL_TYPE = 'Cat' or ANIMAL_TYPE = 'Dog'
order by ANIMAL_TYPE;