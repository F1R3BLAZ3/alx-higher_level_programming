-- This script lists all Comedy shows in the hbtn_0d_tvshows database.

SELECT tv_shows.title
    FROM tv_shows
        JOIN tv_genres ON tv_shows.id = tv_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
