# Write your MySQL query statement below

SELECT sub_weather.id
FROM (
    SELECT
        id,
        temperature
        AS job,
        recorddate,
        LAG(temperature) OVER (ORDER BY recorddate) AS job_prev,
        LAG(recorddate) OVER (ORDER BY recorddate) AS recorddate_prev
    FROM weather
) AS sub_weather
WHERE
    sub_weather.job - sub_weather.job_prev > 0
    AND DATEDIFF(sub_weather.recorddate, sub_weather.recorddate_prev) = 1