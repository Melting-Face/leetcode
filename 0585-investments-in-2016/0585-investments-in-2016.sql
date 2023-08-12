# Write your MySQL query statement below
WITH position AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
),
TIV AS (
  SELECT tiv_2015
  FROM Insurance
  GROUP BY tiv_2015
  HAVING COUNT(*) > 1
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
INNER JOIN TIV
    USING (tiv_2015)
INNER JOIN position
    USING (lat, lon)