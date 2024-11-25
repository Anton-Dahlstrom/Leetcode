# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees e
LEFT JOIN (SELECT * FROM Employees) as managers 
ON managers.employee_id = e.manager_id
WHERE e.salary < 30000 AND e.manager_id IS NOT NULL AND managers.employee_id IS NULL
ORDER BY e.employee_id