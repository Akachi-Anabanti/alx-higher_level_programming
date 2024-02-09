-- lists all cities of california that can be found in
-- in the db
SELECT * FROM cities
WHERE state_id=(SELECT id from states
       WHERE name='California')
ORDER BY id ASC
;
