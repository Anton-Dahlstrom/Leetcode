SELECT *
FROM Cinema c
WHERE (c.id % 2) > 0 AND NOT c.description = 'boring'
ORDER BY c.rating DESC;