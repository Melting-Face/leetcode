# Write your MySQL query statement below
WITH PRODUCT_VALUE AS (
    SELECT DISTINCT
        product_id,
        FIRST_VALUE(new_price) OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) FIRST_VALUE_BY_PRODUCT_ID
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT DISTINCT
    product_id,
    COALESCE(
        PRODUCT_VALUE.FIRST_VALUE_BY_PRODUCT_ID,
        PRODUCT_VALUE.FIRST_VALUE_BY_PRODUCT_ID,
        10
    ) price
FROM Products
LEFT JOIN PRODUCT_VALUE
USING (product_id)
ORDER BY price DESC;