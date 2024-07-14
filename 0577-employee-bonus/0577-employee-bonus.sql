# Write your MySQL query statement below
select
    employee.name,
    bonus.bonus
from employee
left join bonus
    using (empid)
where 
    bonus.bonus < 1000
    or bonus.bonus is null