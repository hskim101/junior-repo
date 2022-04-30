SELECT I.ID
FROM instructor AS I
EXCEPT
SELECT T.ID
FROM teaches AS T
WHERE EXISTS(SELECT I.ID
	       FROM instructor AS I)