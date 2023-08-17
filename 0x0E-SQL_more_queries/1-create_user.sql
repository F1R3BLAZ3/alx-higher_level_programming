-- Script to create MySQL server user user_0d_1 with privileges

-- Check if the user user_0d_1 already exists
SELECT 1 INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_1';

-- If the user doesn't exist, create the user
SET @create_user_query = '';
IF @user_exists IS NULL THEN
    SET @create_user_query = 'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';';
    PREPARE create_user_stmt FROM @create_user_query;
    EXECUTE create_user_stmt;
    DEALLOCATE PREPARE create_user_stmt;
END IF;

-- Grant all privileges to user_0d_1
SET @grant_privileges_query = 'GRANT ALL PRIVILEGES ON *.* TO \'user_0d_1\'@\'localhost\';';
PREPARE grant_privileges_stmt FROM @grant_privileges_query;
EXECUTE grant_privileges_stmt;
DEALLOCATE PREPARE grant_privileges_stmt;
