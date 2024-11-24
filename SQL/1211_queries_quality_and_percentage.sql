# Write your MySQL query statement below
SELECT q.query_name,
ROUND(AVG(q.rating/q.position),2) as quality, 
ROUND(SUM(IF(q.rating < 3, 1,0)) * 100 /COUNT(*),2) as poor_query_percentage
FROM Queries q
WHERE NOT q.query_name IS null
GROUP BY q.query_name;