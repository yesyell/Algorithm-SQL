select BOARD_ID, WRITER_ID, TITLE, PRICE, 
    case 
        when status = 'SALE' then '판매중'
        when status = 'RESERVED' then '예약중'
        when status = 'DONE' then '거래완료'
    end STATUS
from USED_GOODS_BOARD
where created_date = '2022-10-05'
order by 1 desc