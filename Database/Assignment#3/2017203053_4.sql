WITH switch_id(id1,id2) AS
	(SELECT ID1,ID2
	 FROM people_likes)

SELECT COUNT(A.name), A.name
FROM (SELECT DISTINCT L.ID1,L.ID2,S.id1,S.id2, M.name
	  FROM people_main AS M, switch_id AS S, people_likes AS L
	  WHERE (L.ID1=S.id2 AND L.ID2=S.id1) AND L.ID1=M.ID) AS A
GROUP BY A.name
ORDER BY COUNT(A.name) DESC;