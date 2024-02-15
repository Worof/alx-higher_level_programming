-- Lists all genres by their rating sum, sorted in descending order
SELECT g.name, SUM(r.rating) AS rating
FROM tv_genres g
JOIN tv_show_genre sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.tv_show_id = s.id
JOIN tv_show_ratings r ON s.id = r.tv_show_id
GROUP BY g.name
ORDER BY rating DESC;
