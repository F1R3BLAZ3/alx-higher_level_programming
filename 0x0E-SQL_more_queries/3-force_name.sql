-- Script to create the force_name table

-- If the table already exists, the following query will not fail due to the IF NOT EXISTS clause
CREATE TABLE IF NOT EXISTS force_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
