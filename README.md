# 🎓 Student Management System (Python + MySQL)

A **Command-Line Student Management System** built using Python and MySQL.  
This application allows users to **add, update, delete, search, and display student records** stored in a MySQL database, presented in a clean tabular format using the `tabulate` library.

## 📌 Features

- ➕ Add new student records  
- ✏️ Update student details (Name, Age, Grade, Email)  
- ❌ Delete student records using Student ID  
- 🔍 Search students by **ID** or **Name**  
- 📋 Display all student records  
- 🗄️ Persistent storage using **MySQL database**  
- 🖥️ Interactive and user-friendly CLI menu  


## 🛠️ Technologies Used

- **Python**
- **MySQL**
- **mysql-connector-python**
- **tabulate**

## Application Menu
1. Add Student info
2. Update Student info
3. Delete Student info
4. Find Student info
5. Display all Student info
6. Exit

## Future Enhancements
- Input validation and duplicate checks
- Auto-increment Student ID
- Password-protected admin login
- Export data to CSV or Excel
- GUI or Web-based interface (Flask/Django)

## Preview
![image]()
![image]()
![image]()
![image]()
![image]()


## Project structure
Student-Management-System/
│
├── student_management.py # Main Python program
└── README.md # Project documentation

## 🗄️ Database Setup

### Create Database
- sql
- CREATE DATABASE python;

### Use Database
- USE python

### Create Table
- CREATE TABLE STUDENT (
    STUDENT_ID INT PRIMARY KEY,
    NAME VARCHAR(100),
    AGE INT,
    GRADE VARCHAR(10),
    EMAIL VARCHAR(100)
);

## Installation & Setup
### Install Required Packages
- pip install mysql-connector-python tabulate

## Update Database Credentials
- In the Python file, update:
- database = mysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="python"
)

## Author
Developed by Joyjeet Roy
