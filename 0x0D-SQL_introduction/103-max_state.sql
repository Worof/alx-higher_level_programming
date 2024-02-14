-- 103-max_state.sql

SELECT state, MAX(temperature) AS max_temp
FROM temperatures  -- Replace 'temperatures' with the actual table name
GROUP BY state
ORDER BY state;
