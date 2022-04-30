SELECT DISTINCT I.ID, I.name, I.dept_name
FROM instructor AS I, teaches AS T
WHERE I.ID=T.ID AND T.course_id in (SELECT course_id
			           FROM course
			           WHERE course_id LIKE 'CS-1%')