# Write your MySQL query statement below
with first_orders as (
    select
        delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date,
        row_number() over(partition by customer_id order by order_date) as row_num
    from delivery
)

select
    round(
        sum(case when order_date = customer_pref_delivery_date then 1 end)
        / count(*) * 100,
        2
    ) as immediate_percentage
from first_orders
where row_num = 1