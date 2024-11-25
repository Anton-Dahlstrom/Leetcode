# Write your MySQL query statement below
WITH ranking AS(
    SELECT *, COUNT(num) as c
    FROM MyNumbers
    GROUP BY num
    ORDER BY COUNT(num) ASC, num DESC
    LIMIT 1
)
SELECT IF(ranking.c < 2, ranking.num, null) as num
FROM ranking