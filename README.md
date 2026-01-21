# Student Management System (Python + MySQL)

A **Command-Line Student Management System** built using Python and MySQL.  
This application allows users to **add, update, delete, search, and display student records** stored in a MySQL database, presented in a clean tabular format using the `tabulate` library.

## Features

- Add new student records  
- Update student details (Name, Age, Grade, Email)  
- Delete student records using Student ID  
- Search students by **ID** or **Name**  
- Display all student records  
- Persistent storage using **MySQL database**  
- Interactive and user-friendly CLI menu  


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
![image](https://github.com/JoyjeetR/Command-Line-Student-Management-System/blob/main/img/Preview1.png) 
![image](https://github.com/JoyjeetR/Command-Line-Student-Management-System/blob/main/img/Preview2.png)
![image](https://github.com/JoyjeetR/Command-Line-Student-Management-System/blob/main/img/Preview3.png)
![image](https://github.com/JoyjeetR/Command-Line-Student-Management-System/blob/main/img/Preview4.png)
![image](https://github.com/JoyjeetR/Command-Line-Student-Management-System/blob/main/img/Preview5.png)


## Project structure
Student-Management-System/<br>
│<br>
├── student_management.py # Main Python program<br>
└── README.md # Project documentation

## Database Setup
- Create a database in sql 'name'
- Create Table inside 'name' containing id, name, email, age, grade columns

## Installation & Setup
- Install mysql-connector-python tabulate 

## Update Database Credentials
- Update the database connect as per your details
- Insert your host, user, password and database in sql.connect

## Author
Developed by Joyjeet Roy
