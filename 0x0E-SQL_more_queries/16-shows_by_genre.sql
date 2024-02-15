-- Lists all shows and their genres from the hbtn_0d_tvshows database
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genre sg ON s.id = sg.tv_show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
