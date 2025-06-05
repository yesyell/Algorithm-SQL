# select ugb.TITLE, ugb.BOARD_ID, ugr.REPLY_ID, ugr.WRITER_ID, ugr.CONTENTS, 
#     date_format(ugr.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
# from USED_GOODS_BOARD as ugb, USED_GOODS_REPLY as ugr
# where ugb.BOARD_ID = ugr.BOARD_ID and ugr.CREATED_DATE like '2022-10%'
# order by 6 asc, 1 asc

select b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, 
    date_format(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as b, USED_GOODS_REPLY as r
where b.BOARD_ID = r.BOARD_ID and b.CREATED_DATE like '2022-10%'
order by date_format(r.CREATED_DATE, '%Y-%m-%d') asc, b.TITLE asc;