-- Lists all the cities of California from the hbtn_0d_usa database, sorted by cities.id

SELECT id, name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    );
