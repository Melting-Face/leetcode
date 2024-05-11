with employees as (
    select
        department.name as "Department",
        employee.name as "Employee",
        employee.salary as "Salary",
        dense_rank() over (
            partition by employee.departmentid
            order by salary desc
        ) as "rank_num"
    from
        employee as employee
    inner join department as department
        on employee.departmentid = department.id
)

select
    department,
    employee,
    salary
from
    employees
where
    rank_num <= 3
order by
    department asc,
    salary desc