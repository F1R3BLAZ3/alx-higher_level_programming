-- This script lists all genres of the show Dexter from the hbtn_0d_tvshows database.
-- It assumes the database name is provided as an argument to the mysql command.
-- Query to retrieve genres of the show Dexter
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
