CREATE DATABASE cafe_hub;
USE cafe_hub;

CREATE TABLE employee (
    empId VARCHAR(10) PRIMARY KEY, 
    empName VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phoneNumber CHAR(8) NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    CHECK (phoneNumber REGEXP '^[89][0-9]{7}$') 
);

CREATE TABLE cafe (
    cafeId CHAR(36) PRIMARY KEY,
    cafeName VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    logo VARCHAR(255), 
    location VARCHAR(200) NOT NULL
);

CREATE TABLE employee_cafe (
    empId VARCHAR(10) PRIMARY KEY,
    cafeId CHAR(36),
    startDate DATE NOT NULL,
    FOREIGN KEY (empId) REFERENCES employee(empId) ON DELETE CASCADE,
    FOREIGN KEY (cafeId) REFERENCES cafe(cafeId) ON DELETE CASCADE
);