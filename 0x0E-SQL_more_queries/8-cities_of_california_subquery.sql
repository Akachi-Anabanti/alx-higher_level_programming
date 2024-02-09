-- lists all cities of california that can be found in
-- in the db
USE hbtn_0d_usa;
SELECT * FROM cities
WHERE state_id=(SELECT id from states
       WHERE name='California');
