-- Script: 0-privileges.sql
-- Task: List privileges of MySQL users user_0d_1 and user_0d_2 on localhost

-- Connect to the MySQL server
USE mysql;

-- List privileges for user user_0d_1
SELECT * FROM user WHERE user = 'user_0d_1';

-- List privileges for user user_0d_2
SELECT * FROM user WHERE user = 'user_0d_2';

-- Disconnect from the MySQL server
QUIT;
