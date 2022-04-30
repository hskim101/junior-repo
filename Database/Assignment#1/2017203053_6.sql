SELECT DISTINCT S.name
FROM takes AS T, course AS C, student AS S
WHERE T.course_ID= C.course_ID AND C.dept_name='Comp. Sci.' AND T.ID=S.ID