# Write your MySQL query statement below
SELECT r.contest_id , ROUND(COUNT(u.user_id)/(SELECT COUNT(*) FROM Users),4)*100 as percentage
FROM Register r
JOIN Users u ON u.user_id = r.user_Id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC