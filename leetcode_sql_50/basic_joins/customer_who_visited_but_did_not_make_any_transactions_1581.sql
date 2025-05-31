SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
WHERE NOT EXISTS(
    SELECT 1   
    FROM Transactions t
    WHERE v.visit_id = t.visit_id
)
GROUP BY v.customer_id;
-- WHERE NOT EXISTS 這應該是最快的方法

-- ----------------------------------------------------
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;
-- 如果左邊的有null，會報錯。但是這情況中只有去營行，才會有交易紀錄
-- 同一個visit_id有重複的交易沒關係，目的是為了找出一個visit_id不能有交易

SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN (SELECT DISTINCT visit_id FROM Transactions) t
    ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;



-- ----------------------------------------------------
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (
    SELECT visit_id FROM Transactions
)
GROUP BY v.customer_id;



-- SELECT 1  
-- 這編寫什麼都沒差，任何一筆資料符合條件，就回傳 TRUE

-- GROUP BY customer_id ＋ COUNT(*) AS count_no_trans
-- 要先分組，接著算數量