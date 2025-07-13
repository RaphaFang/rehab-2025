WITH temp AS (
    SELECT MIN(id) as keep_id
    FROM Person
    GROUP BY email
)
DELETE FROM Person
WHERE id not in (SELECT keep_id FROM temp);

-- 他沒有辦法直接 drop duplicate
-- 所以要透過 CTE 先建立一個只包含最小數值的表，作為附表
-- 接著透過主表，替除不在附表裡面的