DELETE FROM student
WHERE student.ID in (SELECT I.ID
			 		 FROM instructor AS I
					 WHERE CAST(I.ID AS INTEGER) <=60000);