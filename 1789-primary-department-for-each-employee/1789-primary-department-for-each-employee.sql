# Write your MySQL query statement below
select
    distinct
    employee_id,
    first_value(department_id) over(
        partition by employee_id 
        order by primary_flag
    ) as department_id
from employee