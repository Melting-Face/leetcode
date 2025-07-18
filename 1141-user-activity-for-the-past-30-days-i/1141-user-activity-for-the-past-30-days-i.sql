# Write your MySQL query statement below
select
    activity_date as day,
    count(distinct user_id) as active_users
from activity
where activity_date between date('2019-07-27') - interval 29 day
    and date('2019-07-27')
group by 1