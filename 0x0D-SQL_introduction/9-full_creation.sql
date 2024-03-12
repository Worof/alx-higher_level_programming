-- Use IF NOT EXISTS to avoid errors if the table already exists
CREATE TABLE second_table(id INT PRIMARY KEY,
name VARCHAR(25),
score INT);

-- Insert records into second_table
-- Use INSERT IGNORE to avoid errors if a record already exists
-- Alternatively, you could use ON DUPLICATE KEY UPDATE to update existing records
-- but since the task does not specify handling duplicates, IGNORE will suffice.

INSERT INTO second_table (id, name, score) VALUES (1, "John", 10),
 (2, "Alex", 3),
 (3, "Bob", 14),
 (4, "George", 8);
