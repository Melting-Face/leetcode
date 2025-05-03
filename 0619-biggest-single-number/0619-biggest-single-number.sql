# Write your MySQL query statement below
select
    max(single_nums.num) as num
from (
    select
        num
    from mynumbers
    group by 1
    having count(*) = 1
) as single_nums