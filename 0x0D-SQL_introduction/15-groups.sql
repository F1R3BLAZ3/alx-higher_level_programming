-- Script to list the number of records with the same score in the second_table of the hbtn_0c_0 database
-- The result will display the score and the number of records for each score
-- The list will be sorted by the number of records in descending order

-- Retrieve the score and the corresponding record count from the second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
