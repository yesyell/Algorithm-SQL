select DR_NAME, DR_ID, MCDP_CD, 
    date_format(HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
from DOCTOR
where MCDP_CD in ('CS', 'GS')
order by 4 desc, 1 asc;