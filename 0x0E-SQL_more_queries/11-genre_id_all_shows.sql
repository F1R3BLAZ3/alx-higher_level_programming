-- Script to list shows and their genre IDs from the hbtn_0d_tvshows database
-- SQL keywords are in uppercase

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
