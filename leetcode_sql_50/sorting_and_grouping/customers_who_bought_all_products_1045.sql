SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product);

-- WHERE 不能放在 GROUP BY 後面
-- 如果單純算數字，也不用加上 as 來標記欄位