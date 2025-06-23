WITH ranked AS (
    SELECT
        employee_id, 
        department_id,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id
            ORDER BY
                CASE
                    WHEN primary_flag = "Y" THEN 1 ELSE 2
                END
        ) AS rn
    FROM Employee
)
SELECT employee_id, department_id
FROM ranked
WHERE rn = 1;

-- 會思考錯誤的地方是
-- ORDER BY 下方的 CASE 是處理排序
    -- 就想像我現在有一個排序欄位，他會是如果有 Y 則 1，其他全是 2
    -- 之後，再來編輯他的 rn 欄位，這時會案順序 1, 2, 3, ...
    -- Thus, 即便CASE欄位得到 2 ，也就是只有一筆
    -- 在 rn 排序也會是 1 開始

-- --------------------------------------------------------------------
-- SELECT 
--     employee_id,
--     CASE
--         WHEN COUNT(department_id) > 1 THEN SELECT department_id WHERE primary_flag = "Y"
--         ELSE SELECT department_id WHERE primary_flag = "N"
--     END AS department_id
-- FROM Employee
-- GROUP BY employee_id;