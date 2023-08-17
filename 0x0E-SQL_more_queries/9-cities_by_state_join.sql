-- This SQL script lists all cities contained in the database hbtn_0d_usa,
-- displaying cities.id, cities.name, and states.name for each record.
-- The results are sorted in ascending order by cities.id.

-- Assuming the database name is passed as an argument to the MySQL command.

USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
