# Write your MySQL query statement below
WITH managers AS (SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) > 4)

SELECT e.name
FROM Employee e
INNER JOIN managers m ON m.managerId = e.id;