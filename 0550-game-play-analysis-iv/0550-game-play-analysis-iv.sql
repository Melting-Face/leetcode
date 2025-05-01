# Write your MySQL query statement below
with consecutive_event_dates as (
    select
        player_id,
        event_date,
        lead(event_date) over (partition by player_id order by event_date) as next_event_date,
        row_number() over (partition by player_id order by event_date) as row_num
    from activity
)

select
    round(
        count(distinct case when datediff(next_event_date, event_date) = 1 and row_num = 1 then player_id end)
        / count(distinct player_id),
        2
    ) as fraction
from consecutive_event_dates