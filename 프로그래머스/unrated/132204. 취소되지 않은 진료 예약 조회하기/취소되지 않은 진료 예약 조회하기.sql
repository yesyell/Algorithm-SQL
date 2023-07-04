select apnt_no, pt_name, p.pt_no, 
    d.mcdp_cd, dr_name, apnt_ymd
from appointment a
join patient p
on p.pt_no = a.pt_no
join doctor d
on d.dr_id = a.mddr_id
where d.mcdp_cd = 'CS'
and apnt_cncl_yn = 'N'
and apnt_ymd like '2022-04-13%'
order by 6;