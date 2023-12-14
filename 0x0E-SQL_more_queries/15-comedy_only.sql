-- uses the hbtn_0d_tvshows database to lists all comedy
SELECT title FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY title;
