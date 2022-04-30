SELECT max(cnt) AS "최대수강인원", min(cnt) AS "최소수강인원"
FROM (SELECT course_id,count(course_id) AS cnt, sec_id
	  FROM takes
	  GROUP BY course_id,sec_id)
WHERE cnt>0