/* Write your PL/SQL query statement below */
SELECT
    teacher_id,
    sum(cnt) AS cnt
FROM (
    SELECT
        teacher_id,
        1 AS cnt
    FROM teacher
    GROUP BY teacher_id, subject_id
)
GROUP BY teacher_id, cnt