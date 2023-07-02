select USER_ID, NICKNAME, 
    concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) 전체주소, 
    concat('010-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4)) 전화번호
from USED_GOODS_BOARD b
join USED_GOODS_USER u
on writer_id = user_id
group by 1
having count(*) >= 3
order by 1 desc;