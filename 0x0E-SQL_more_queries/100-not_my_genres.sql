-- Script to list all tv shows and genre id
SELECT tv_genres.name AS 'name'
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT tv_show_genres.genre_id FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
ORDER BY name
