SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;



-- ASC 由小到大，同長可以不必寫
-- DESC 

-- DISTINCT 排除重複