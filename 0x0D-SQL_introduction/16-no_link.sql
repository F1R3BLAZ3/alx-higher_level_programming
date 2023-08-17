-- Script to list records from second_table with certain conditions
-- List records from second_table with non-empty name values
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
