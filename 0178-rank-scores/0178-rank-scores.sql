/* Write your PL/SQL query statement below */
SELECT
score,
DENSE_RANK() OVER (ORDER BY score desc) "rank"
FROM Scores