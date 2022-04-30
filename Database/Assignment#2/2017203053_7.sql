UPDATE instructor
SET salary = 50000 * (SELECT COUNT(T.course_id)
					  FROM instructor AS I, teaches AS T
					  WHERE I.ID = T.ID AND instructor.ID = I.ID
					  GROUP BY I.ID);
UPDATE instructor
SET salary=30000
WHERE instructor.salary IS NULL;
