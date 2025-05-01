# Write your MySQL query statement below
with managers as (
    select
        m.id,
        m.name
    from employee m
    left join employee e
        on m.id = e.managerid
    group by 1, 2
    having count(e.id) >= 5
)

select
    name
from managers