SELECT T.ID ,SUM(C.credits)
FROM takes AS T, course AS C
WHERE T.course_ID=C.course_ID
GROUP BY T.ID