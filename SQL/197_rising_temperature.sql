# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
LEFT JOIN Weather w2 ON w2.recordDate + INTERVAL 1 DAY = w1.recordDate
WHERE w1.temperature > w2.temperature