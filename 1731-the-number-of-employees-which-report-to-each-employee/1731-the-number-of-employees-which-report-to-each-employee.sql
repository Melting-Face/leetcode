# Write your MySQL query statement below
select
    manager.employee_id,
    manager.name,
    count(manager.employee_id) as reports_count,
    round(avg(employee.age)) as average_age
from employees as manager
left join employees as employee
    on manager.employee_id = employee.reports_to
where employee.reports_to is not null
group by 1, 2
order by 1