-- list all records of the table with name
-- display results in descending score
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
