-- Script to create the database hbtn_0c_0 if it doesn't exist

-- Connect to MySQL server as root
-- You will be prompted to enter your MySQL root password
mysql -u root -p << EOF
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
-- Exit the MySQL session
EXIT;
EOF
