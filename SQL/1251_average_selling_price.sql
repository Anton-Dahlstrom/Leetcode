WITH sold AS(
    SELECT u.units * p.price as total_sold, u.* 
    FROM UnitsSold u
    LEFT JOIN Prices p ON p.product_id = u.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
),
avg_price AS(
    SELECT s.product_id, ROUND(SUM(s.total_sold) / SUM(s.units), 2) as average_price
    FROM sold as s
GROUP BY s.product_id
)
SELECT p.product_id, IF(a.average_price IS null, 0, a.average_price) as average_price
FROM Prices p
LEFT JOIN avg_price a ON a.product_id = p.product_id
GROUP BY p.product_id