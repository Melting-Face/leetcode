# Write your MySQL query statement below
select
    register.contest_id,
    round(
        count(register.contest_id) 
        / (select count(*) from users)
        * 100,
        2
    ) as percentage
from register
group by 1
order by 2 desc, 1