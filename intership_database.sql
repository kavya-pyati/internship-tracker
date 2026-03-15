CREATE DATABASE internship_tracker;
USE internship_tracker;

CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100),
    status VARCHAR(50),
    notes TEXT
);

SELECT * FROM applications;
