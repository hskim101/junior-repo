INSERT INTO student (ID, name, dept_name)
	SELECT I.ID, I.name, I.dept_name
	FROM instructor AS I
	WHERE CAST(I.ID AS INTEGER)<=60000;

UPDATE student
SET tot_cred=0
WHERE student.ID in (SELECT I.ID
					 FROM instructor AS I
					 WHERE CAST(I.ID AS INTEGER)<=60000);