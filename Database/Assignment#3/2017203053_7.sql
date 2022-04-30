With give(ID1,ID2,ID,name,occupation,birth_year) AS
		(SELECT *
		 FROM people_likes AS L, people_main AS M
		 WHERE L.ID1=M.ID),
	take(ID1,ID2,ID,name,occupation,birth_year) AS
		(SELECT *
		 FROM people_likes AS L, people_main AS M
		 WHERE L.ID2=M.ID)

SELECT DISTINCT G.name, G.ID, T.ID, T.name
FROM people_likes AS L, people_friends AS F, give AS G, take AS T
WHERE (L.ID1=F.ID1 AND L.ID2 != F.ID2) AND (L.ID1=G.ID AND L.ID2=T.ID)
EXCEPT
SELECT DISTINCT G.name,F.ID1,F.ID2,T.name
FROM people_friends AS F, give AS G, take AS T