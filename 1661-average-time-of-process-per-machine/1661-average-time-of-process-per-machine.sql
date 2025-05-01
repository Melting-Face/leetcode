# Write your MySQL query statement below
with machine_processes as (
    select
        machine_id,
        process_id,
        sum(
            if(activity_type = 'end', timestamp, 0)
            - if(activity_type = 'start', timestamp, 0)
        ) as processing_time
    from activity
    group by 1, 2
)

select
    machine_id,
    round(avg(processing_time), 3) as processing_time
from machine_processes
group by 1