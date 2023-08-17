-- Lists all privileges of the MySQL Users `user_0d_1`
-- and `user_0d_2` in `localhost`.
-- Show privileges for user_0d_1
SELECT Grant_priv 
FROM user
WHERE user = 'user_0d_1' AND host = 'localhost';

-- Show privileges for user_0d_2
SELECT Grant_priv 
FROM user
WHERE user = 'user_0d_2' AND host = 'localhost';
