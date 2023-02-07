CREATE USER 'fastapi'@'localhost' IDENTIFIED BY 'fastapi_pass';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD
on *.* TO 'fastapi'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS cosmetic_shop;