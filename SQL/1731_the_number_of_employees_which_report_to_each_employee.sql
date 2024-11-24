# Write your MySQL query statement below
SELECT 
    m.employee_id as employee_id, 
    m.name, 
    COUNT(e.reports_to) AS reports_count, 
    ROUND(AVG(e.age)) AS average_age
FROM Employees e
INNER JOIN (SELECT name, employee_id FROM Employees) AS m ON m.employee_id = e.reports_to
GROUP BY e.reports_to
ORDER BY m.employee_id;