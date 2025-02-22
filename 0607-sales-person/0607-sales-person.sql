# Write your MySQL query statement below
select
    SalesPerson.name
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders
    inner join Company
        using (com_id)
    where Company.name = 'RED'
)