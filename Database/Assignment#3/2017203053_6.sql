With give(ID1,ID2,ID,name,occupation,birth_year) AS
		(SELECT *
		 FROM people_likes AS L, people_main AS M
		 WHERE L.ID1=M.ID),
	take(ID1,ID2,ID,name,occupation,birth_year) AS
		(SELECT *
		 FROM people_likes AS L, people_main AS M
		 WHERE L.ID2=M.ID)
	
SELECT DISTINCT T.name,T.birth_year
FROM give AS G, take AS T
WHERE (G.ID1=T.ID1 AND G.ID2=T.ID2) AND (G.birth_year > T.birth_year)
ORDER BY T.name ASC;