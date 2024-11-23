# Write your MySQL query statement below
WITH confirmed_count AS (SELECT c.user_id,  COUNT(*) AS confirmed
FROM Confirmations c
WHERE c.action = 'confirmed'
GROUP BY c.user_id),

total_count AS (SELECT t.user_id, COUNT(*) AS total
FROM Confirmations t
GROUP BY t.user_id), 

ratio_or_null AS (select t.user_id as user_id, ROUND(c.confirmed / t.total, 2) as ratio
FROM total_count t
LEFT JOIN confirmed_count c ON t.user_id = c.user_id
)

SELECT s.user_id, IFNULL(r.ratio, 0) AS confirmation_rate
FROM Signups s
LEFT JOIN ratio_or_null r on r.user_id = s.user_id