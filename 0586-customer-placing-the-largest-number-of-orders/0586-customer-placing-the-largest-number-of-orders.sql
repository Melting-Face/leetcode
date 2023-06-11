/* Write your PL/SQL query statement below */
SELECT customer_number
FROM (
    SELECT customer_number
    FROM orders
    GROUP BY customer_number
    ORDER BY count(*) DESC
) WHERE rownum <= 1