with requesters as (
    select
        requester_id id,
        count(*) as num
    from requestaccepted
    group by
        requester_id
),

accepters as (
    select
        accepter_id id,
        count(*) as num
    from requestaccepted
    group by
        accepter_id
),

ids as (
    select id
    from
        requesters
    union
    select id
    from accepters
)

select
    ids.id,
    COALESCE(requesters.num, 0) + COALESCE(accepters.num, 0) as num
from ids
left join requesters
    on ids.id = requesters.id
left join accepters
    on ids.id = accepters.id
order by COALESCE(requesters.num, 0) + COALESCE(accepters.num, 0) desc
limit 1