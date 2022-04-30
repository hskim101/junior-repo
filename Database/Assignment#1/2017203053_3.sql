SELECT DISTINCT C.course_id, C.title
FROM takes AS T, course AS C
WHERE T.ID=45678 AND T.course_id=C.course_id