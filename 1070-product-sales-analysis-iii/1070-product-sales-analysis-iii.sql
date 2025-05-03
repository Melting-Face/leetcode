# Write your MySQL query statement below
with first_sales as (
    select
        product_id,
        year,
        sale_id
    from sales
    group by 1
    having year = min(year)
) 

select
    product_id,
    year as first_year,
    quantity,
    price
from sales
where sale_id in (
    select
        sale_id
    from first_sales
)