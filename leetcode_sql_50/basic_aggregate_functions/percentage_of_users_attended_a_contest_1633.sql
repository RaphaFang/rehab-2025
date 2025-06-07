SELECT r.contest_id, ROUND(COUNT(r.user_id)*100/(SELECT COUNT(u.user_id) FROM Users u),2) AS percentage
FROM Register r
LEFT JOIN Users u
    ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id; -- 這邊的ASC不用寫


-- 我這邊已經重新編輯圖表，這時候再去/COUNT(DISTINCT u.user_id) 作為分母
-- 會得到的不會是原始表格，而是 GROUP BY 得到的東西
-- n / n 當然都會是 1