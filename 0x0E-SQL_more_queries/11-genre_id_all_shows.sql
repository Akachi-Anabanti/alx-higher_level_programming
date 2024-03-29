-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre
SELECT title, genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
