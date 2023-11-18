--Set up a test database for system

--Create a new database(test)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--Create a new user for database (test)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' 
IDENTIFIED BY 'hbnb_test_pwd';

--Grant hbnb_test read-only permissions to hbnb_test_db (test)
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost'

--Grant hbnb_test all privileges on hbnb_test_db (test)
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost'

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
