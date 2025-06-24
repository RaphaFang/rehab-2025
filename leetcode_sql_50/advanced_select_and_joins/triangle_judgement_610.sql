SELECT x, y, z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
-- 這方式真的聰明太多了
-- ------------------------------------------------------------

WITH n AS (
    SELECT
        x, y, z,
        GREATEST(x, y, z) as g,
        (col1 + col2 + col3) AS total
    FROM Triangle
)
SELECT x, y, z,
    (CASE
        WHEN (total - g) > g THEN "Yes" ELSE "No"
    END) as triangle
FROM n;


-- 沒有辦法橫向的加上三個，所以要 (col1 + col2 + col3) AS total
