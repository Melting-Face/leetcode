# Write your MySQL query statement below
select
    prices.product_id,
    round(
        sum(unitssold.units * prices.price) / sum(unitssold.units), 
        2
    ) as average_price
from prices
left join unitssold
    on 
        prices.product_id = unitssold.product_id
        and 
            unitssold.purchase_date 
            between prices.start_date
            and prices.end_date
group by 1