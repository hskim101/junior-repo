SELECT M.title, COUNT(R.rolename)
FROM movies AS M, actors AS A, actor_role AS R
WHERE A.AID=R.AID AND M.MID=R.MID AND A.name='Tilda Swinton'
GROUP BY M.title