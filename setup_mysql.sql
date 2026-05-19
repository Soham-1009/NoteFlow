-- Run this in your MySQL shell before starting the Django app

-- Create the database
CREATE DATABASE IF NOT EXISTS notes_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Create a dedicated user (recommended over using root)
CREATE USER IF NOT EXISTS 'notes_user'@'localhost' IDENTIFIED BY 'your_strong_password';

GRANT ALL PRIVILEGES ON notes_db.* TO 'notes_user'@'localhost';

FLUSH PRIVILEGES;
SHOW DATABASES LIKE 'notes_db';
