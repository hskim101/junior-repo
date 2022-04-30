UPDATE student
SET tot_cred = (SELECT sum(C.credits)
				FROM takes AS T, course AS C
				WHERE T.grade != 'F' AND T.grade IS NOT NULL AND T.course_id=C.course_id AND student.ID=T.ID
				GROUP BY T.ID);

UPDATE student
SET tot_cred = 0
WHERE tot_cred IS NULL;
