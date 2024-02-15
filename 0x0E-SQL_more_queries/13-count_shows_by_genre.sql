--a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.genre AS genre, COUNT(sg.tv_show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genre sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.tv_show_id = s.id
GROUP BY g.genre
HAVING COUNT(sg.tv_show_id) > 0
ORDER BY COUNT(sg.tv_show_id) DESC;
