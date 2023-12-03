# Write your MySQL query statement below
WITH user_confirmation AS (
  SELECT
    user_id,
    COUNT(CASE action WHEN 'confirmed' THEN 1 ELSE NULL END) AS num,
    COUNT(*) AS total
  FROM signups
  LEFT JOIN confirmations
  USING (user_id)
  GROUP BY user_id
)

SELECT
  user_id,
  ROUND(num / total, 2) AS confirmation_rate
FROM user_confirmation;