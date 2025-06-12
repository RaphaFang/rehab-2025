SELECT 
q.query_name,
ROUND(SUM(q.rating/q.position) / COUNT(q.query_name),2) as quality,
ROUND(SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END)/COUNT(*)* 100,2) as poor_query_percentage
FROM Queries q
GROUP BY q.query_name;



-- SELECT q.query_name,(SUM(q.rating/q.position) / (SELECT COUNT(*) from Queries)) as quality
-- FROM Queries q
-- GROUP BY q.query_name;

