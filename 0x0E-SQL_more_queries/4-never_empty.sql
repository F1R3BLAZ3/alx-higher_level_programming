-- Script: Create id_not_null Table
-- Description: Creates the id_not_null table with specified columns and default values
-- Usage: mysql -u <username> -p <database_name> < script.sql

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
