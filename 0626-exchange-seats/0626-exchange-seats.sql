# Write your MySQL query statement below
select 
    s1.id,
    if(
        s2.student is null,
        s1.student,
        s2.student
    ) as student
from Seat as s1
left join Seat as s2
    on (s1.id + 1) div 2 = (s2.id + 1) div 2
    and (s1.id + 1) mod 2 != (s2.id + 1) mod 2