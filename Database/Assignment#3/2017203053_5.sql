SELECT A.name,A.occupation
FROM (SELECT F.ID1, F.ID2, M.ID,M.name, count(M.name) AS cnt, M.occupation
	  FROM people_friends AS F, people_main AS M
	  WHERE F.ID1=M.ID 
	  GROUP BY M.name) AS A
WHERE A.cnt >=3