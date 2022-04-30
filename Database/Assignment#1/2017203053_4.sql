SELECT SUM(C.credits)
FROM takes AS T, course AS C
WHERE T.ID=45678 AND T.course_ID = C.course_ID