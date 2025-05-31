SELECT w.id
FROM Weather today
JOIN Weather yesterday
    ON today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
WHERE today.temperature > yesterday.temperature;


-- LEFT JOIN Weather yesterday
--     ON today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
-- WHERE today.temperature > yesterday.temperature;
-- 不用設定條件也不會報錯，是因為他WHERE比較時，或比較有數值的

-- 但是還是用 JOIN 就好
-- 兩者都有的數據才會建立table
