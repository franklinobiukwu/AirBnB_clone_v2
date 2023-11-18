--Set up a user and a database for system

--Create a new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--Create a new user for database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

--Grant hbnb_dev read-only permissions to performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';

--Grant hbnb_dev all privileges on hbnh_dev_db
GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
