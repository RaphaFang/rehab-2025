SELECT COALESCE((
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
    ORDER BY num DESC
    LIMIT 1
), NULL) as result;

-- 重點，沒有辦法直接的標示出 NULL，要透過這方式強調標示