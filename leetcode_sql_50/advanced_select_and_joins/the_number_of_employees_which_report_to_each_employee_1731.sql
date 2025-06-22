SELECT 
    e2.employee_id,
    e2.name, 
    COUNT(e1.employee_id) as reports_count,
    ROUND(AVG(e1.age),0) as average_age
FROM employees e1
JOIN employees e2
    ON e1.reports_to = e2.employee_id
GROUP BY e2.employee_id
ORDER BY employee_id;

-- ------------------------------------------------------------------------
-- 使用子查詢，會明顯慢兩倍
SELECT 
    e.reports_to as employee_id,
    (SELECT ee.name FROM Employees ee WHERE ee.employee_id = e.reports_to) as name,
    COUNT(e.reports_to) as reports_count,
    ROUND(AVG(e.age), 0) as average_age
FROM Employees e
WHERE e.reports_to is NOT NULL
GROUP BY e.reports_to
ORDER BY reports_count DESC;

-- (SELECT ee.name FROM E ......
-- 這邊要選定一個欄位，不能直接回傳 ＊