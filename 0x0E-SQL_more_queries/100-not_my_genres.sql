-- Lists all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
WHERE g.id NOT IN (
    SELECT sg.genre_id
    FROM tv_shows s
    JOIN tv_show_genre sg ON s.id = sg.tv_show_id
    WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;
