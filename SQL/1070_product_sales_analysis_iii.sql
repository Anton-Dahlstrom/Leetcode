# Write your MySQL query statement below
WITH min_year AS (
    SELECT product_id, min(year) as y
    FROM Sales
    GROUP BY product_id
    )

SELECT s.product_id, min_year.y as first_year, SUM(s.quantity) as quantity, s.price
FROM Sales s
RIGHT JOIN min_year ON min_year.product_id = s.product_id AND min_year.y = s.year
GROUP BY s.product_id, s.price