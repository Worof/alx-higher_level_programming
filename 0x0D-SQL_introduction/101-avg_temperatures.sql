-- 101-avg_temperatures.sql

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures  -- Replace 'temperatures' with the actual table name
GROUP BY city
ORDER BY avg_temp DESC;
