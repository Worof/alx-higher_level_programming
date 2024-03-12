-- 16-no_link.sql

-- List records with a name value, displaying score and name, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;