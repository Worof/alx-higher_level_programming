-- 102-top_city.sql

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures  -- Replace 'temperatures' with your actual table name
WHERE MONTH(date_field) IN (7, 8)  -- Assuming 'date_field' is the name of the date or month column
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
