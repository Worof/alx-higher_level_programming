--a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.name
FROM tv_genres g
JOIN tv_show_genre sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.tv_show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
