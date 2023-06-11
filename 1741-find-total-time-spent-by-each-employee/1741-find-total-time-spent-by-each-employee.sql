/* Write your PL/SQL query statement below */
SELECT
    "day",
    emp_id,
    SUM(total_time) AS total_time
FROM (
    SELECT
        TO_CHAR(event_day, 'YYYY-MM-DD') AS "day",
        emp_id,
        out_time - in_time AS total_time
    FROM employees
    GROUP BY event_day, emp_id, in_time, out_time
)
GROUP BY "day", emp_id
ORDER BY total_time DESC