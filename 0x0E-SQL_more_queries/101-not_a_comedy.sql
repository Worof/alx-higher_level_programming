-- Lists all shows without the genre Comedy
SELECT s.title
FROM tv_shows s
WHERE s.id NOT IN (
  SELECT sg.tv_show_id
  FROM tv_show_genre sg
  JOIN tv_genres g ON sg.genre_id = g.id
  WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
