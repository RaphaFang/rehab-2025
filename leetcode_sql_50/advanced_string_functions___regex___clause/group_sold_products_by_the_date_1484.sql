-- With temp AS (
--     SELECT *
--     FROM Activities
-- )

SELECT
    sell_date,
    COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product) as products
FROM Activities
GROUP BY sell_date;

-- 不需要透過CTE建立附表排查，因為我沒有要delete
-- 直接透過 DISTINCT 就可以