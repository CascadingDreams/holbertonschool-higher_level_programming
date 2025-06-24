-- Lists all records from second_table showing score and name
-- excludes rows where name is NULL/empty
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;