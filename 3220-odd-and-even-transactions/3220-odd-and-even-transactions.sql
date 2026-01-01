# Write your MySQL query statement below
select
    transaction_date,
    coalesce(sum(if(amount % 2 = 1, amount, 0)), 0) as odd_sum,
    coalesce(sum(if(amount % 2 = 0, amount, 0)), 0) as even_sum
from transactions
group by 1
order by 1