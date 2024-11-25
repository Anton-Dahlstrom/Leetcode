# Write your MySQL query statement below
WITH multi_dep AS(
    SELECT * 
    FROM Employee
    WHERE primary_flag = 'Y'
)
SELECT 
    e.employee_id, 
    IF(multi_dep.employee_id IS NOT null, multi_dep.department_id, e.department_id) as department_id
FROM Employee e
lEFT JOIN multi_dep ON multi_dep.employee_id = e.employee_id
GROUP BY e.employee_id