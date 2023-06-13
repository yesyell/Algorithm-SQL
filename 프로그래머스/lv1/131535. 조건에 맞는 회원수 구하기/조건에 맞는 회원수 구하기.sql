select count(*) as USERS
from USER_INFO
where extract(year from JOINED) = 2021
    and AGE between 20 and 29