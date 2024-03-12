-- Lists all Comedy shows in the hbtn_0d_tvshows database
SELECT s.title
FROM tv_shows s
JOIN tv_show_genre sg ON s.id = sg.tv_show_id
JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
