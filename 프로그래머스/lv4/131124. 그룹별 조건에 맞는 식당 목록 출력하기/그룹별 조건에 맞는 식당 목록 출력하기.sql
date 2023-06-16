select member_name, review_text, 
    date_format(review_date, '%Y-%m-%d') as review_date
from member_profile p
join (
    select
        member_id, review_text, review_date,
        count(review_id) over (partition by member_id) as review_count
    from rest_review) r
on p.member_id = r.member_id
where review_count = (
    select count(*)
    from rest_review
    group by member_id
    order by count(*) desc
    limit 1)
order by review_date, review_text