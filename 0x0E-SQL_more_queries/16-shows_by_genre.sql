-- This script lists all TV shows and their linked genres from the hbtn_0d_tvshows database.

-- SQL query to list TV shows and their linked genres.
SELECT
    tv_shows.title AS show_title,
    IFNULL(GROUP_CONCAT(tv_genres.name ORDER BY tv_genres.name ASC SEPARATOR ', '), 'NULL') AS genre_names
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY
    tv_shows.id
ORDER BY
    show_title ASC, genre_names ASC;
