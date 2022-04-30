SELECT I.ID, I.name
FROM instructor AS I,teaches AS T
EXCEPT
SELECT T.ID, I.name
FROM teaches AS T, instructor AS I
WHERE I.ID=T.ID