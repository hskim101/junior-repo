SELECT DISTINCT A.name, M.title
FROM actors AS A natural left outer join actor_role AS R natural left outer join movies AS M