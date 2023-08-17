-- Lists all the cities of California from the hbtn_0d_usa database, sorted by cities.id

USE hbtn_0d_usa;

-- First, find the state_id for California
SELECT id INTO @california_id FROM states WHERE name = 'California';

-- Then, list all the cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_id
ORDER BY cities.id;
