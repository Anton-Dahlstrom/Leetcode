# Write your MySQL query statement below
SELECT x, y, z, 
    CASE WHEN x >= y AND x >= z THEN IF(x >= y + z, 'No', 'Yes')
         WHEN y >= x AND y >= z THEN IF(y >= x + z, 'No', 'Yes')
         ELSE IF(z >= x + y, 'No', 'Yes') END AS triangle
FROM Triangle