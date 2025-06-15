SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;

-- ------------------------------------
SELECT class 
FROM (SELECT class, COUNT(*) as c
    FROM Courses
    GROUP BY class
) AS sub_t
WHERE c >=5;

-- 這寫法也可以轉換

WITH sub_t AS (
    SELECT class, COUNT(*) as c
    FROM Courses
    GROUP BY class
)
SELECT class 
FROM Stud
WHERE count >= 5;

-- ------------------------------------
-- ! 不能這樣，then 只能回傳數值
-- SELECT
--     CASE
--         WHEN COUNT(*) >= 5 THEN class
--     END
-- FROM Courses
-- GROUP BY class;