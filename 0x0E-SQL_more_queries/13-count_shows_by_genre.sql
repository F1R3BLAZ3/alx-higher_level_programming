-- List TV Show genres with the number of linked shows
-- Author: Your Name

SELECT genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows.shows
JOIN hbtn_0d_tvshows.show_genres ON shows.id = show_genres.show_id
JOIN hbtn_0d_tvshows.genres ON show_genres.genre_id = genres.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
