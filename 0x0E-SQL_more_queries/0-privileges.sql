-- Script to list privileges of MySQL users user_0d_1 and user_0d_2 on localhost
-- List privileges for user_0d_1
SELECT * 
FROM user
WHERE user = 'user_0d_1'
AND host = 'localhost';

-- List privileges for user_0d_2
SELECT * 
FROM user
WHERE user = 'user_0d_2'
AND host = 'localhost';
