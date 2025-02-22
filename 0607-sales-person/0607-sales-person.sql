# Write your MySQL query statement below
select salesperson.name
from salesperson
where salesperson.sales_id not in (
    select sales_id
    from orders
    inner join company
        using (com_id)
    where company.name = 'RED'
)