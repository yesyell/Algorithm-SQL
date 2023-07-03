select concat('/home/grep/src/', b.board_id, '/', file_id, file_name, file_ext) file_path
from USED_GOODS_BOARD b
join USED_GOODS_FILE f
on b.board_id = f.board_id
where b.board_id = (
    select board_id
    from USED_GOODS_BOARD
    order by views desc
    limit 1
)
order by file_id desc

# /home/grep/src/B0001/IMG_000001photo1.jpg
