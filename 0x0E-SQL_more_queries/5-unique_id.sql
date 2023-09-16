-- Create the unique_id table
CREATE TABLE IF NOT EXISTS unique_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Set the default value of id column to 1
ALTER TABLE unique_id
    ALTER COLUMN id SET DEFAULT 1;

-- Add a unique constraint to ensure id is unique
ALTER TABLE unique_id
    ADD CONSTRAINT uc_unique_id_id UNIQUE (id);

-- Display the structure of the unique_id table
DESCRIBE unique_id;
