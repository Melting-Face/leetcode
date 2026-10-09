# Write your MySQL query statement below

with MoviesAndUsers as (
    select
        name,
        title,
        rating,
        created_at
    from MovieRating
    inner join Users
        using (user_id)
    inner join Movies
        using (movie_id)
),

FirstUser as (
    select 
        name,
        count(*)
    from MoviesAndUsers
    group by 1
    order by 2 desc, 1
    limit 1
),

FirstMovie as (
    select 
        title,
        avg(rating)
    from MoviesAndUsers
    where year(created_at) = 2020
      and month(created_at) = 2
    group by 1
    order by 2 desc, 1
    limit 1
)

select name as results
from FirstUser

union all

select title as results 
from FirstMovie