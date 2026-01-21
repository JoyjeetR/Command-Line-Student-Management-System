# Student management System.
from tabulate import tabulate
import mysql.connector as mysql

# Connecting the 'python' database inside sql where the data is stored 
database = mysql.connect(
    host ="localhost",
    user = "root",
    password = "new_password",
    database = "python"
)
cusor = database.cursor()

# function to add data of the student
def add_student(id,name,age,grade,email):
    # SQL syntax to store data in database
    try:
        cusor.execute(
            "INSERT INTO STUDENT (STUDENT_ID, NAME, AGE, GRADE, EMAIL) VALUES (%s,%s,%s,%s,%s)",
            (id, name, age, grade, email)
        )
        database.commit()
        print("Student added successfully.")
    except mysql.Error as e:
        print("❌ Error:", e , "❌")
    
# Class for the functions which updates a particular data of a student through its ID 
class update:
    # function to update name of student 
    def name(self,id,name):
        cusor.execute("UPDATE STUDENT SET NAME = %s WHERE STUDENT_ID = %s",[name,id])
        database.commit()
    # function to update Age of student 
    def age(self,id,age):
        cusor.execute("UPDATE STUDENT SET AGE = %s WHERE STUDENT_ID = %s",[age,id])
        database.commit()
    # function to update class of student
    def grade(self,id,grade):
        cusor.execute("UPDATE STUDENT SET GRADE = %s WHERE STUDENT_ID = %s",[grade,id])
        database.commit()
    # function to email class of student
    def email(self,id,email):
        cusor.execute("UPDATE STUDENT SET EMAIL = %s WHERE STUDENT_ID = %s",[email,id])
        database.commit()
        
# function for deleting data of a particular student thought its ID
def delete_student(id):
    cusor.execute("DELETE FROM STUDENT WHERE STUDENT_ID = %s",[id])
    database.commit()
    print("Successfully deleted")
    
# class for the functions to find data of student 
class search:
    # function to find data through Name
    def name(self,name):
        cusor.execute("SELECT * FROM STUDENT WHERE NAME = %s",[name])
        self.show(cusor.fetchall())
        
    # function to find data through ID    
    def id(self,id):
        cusor.execute("SELECT * FROM STUDENT WHERE STUDENT_ID = %s",[id])
        self.show(cusor.fetchall())
    
    # Display find info
    def show(self, data):
        if data:
            header = ["ID","Name","Age","Grade","Email"]
            print(tabulate(data,headers=header,tablefmt="fancy_grid"))
        else:
            print("⚠️ !! No record found !! ⚠️")

# function for showing all students data
def display_all():
    cusor.execute("SELECT * FROM STUDENT")
    info = cusor.fetchall()
    header = ["ID","Name","Age","Grade","Email"]
    print(tabulate(info,headers=header,tablefmt="fancy_grid"))
    
while True:
    # Selection Screen
    print("\n1. Add Student info.")   
    print("2. Update Student info.")   
    print("3. Delete Student info.")   
    print("4. Find Student info.")   
    print("5. Display all Student info.")   
    print("6. Exit.")
    # checking the valid value
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("❌ Invalid input ❌")
        continue
    
    match choice:
        case 1:
            # Input Student data to add.
            id = int(input("Enter student id :")) 
            name = (input("Enter student name :")) 
            age = int(input("Enter student age :")) 
            grade = (input("Enter student grade :")) 
            email = (input("Enter student email :"))
            # Executing Adding process 
            add_student(id,name,age,grade,email)
        case 2:
            u1=update()
            # Id to update data
            id = int(input("Enter id to update :"))
            while True:
                # Update choices
                print()
                print("1. Update name")
                print("2. Update age")
                print("3. Update grade")
                print("4. Update email")
                print("5. Exit from update.")
                update_choice = int(input("Enter your choice :"))
                # Inserting and updating New data
                match update_choice:
                    case 1:
                        name = input("Enter name to new name :")
                        u1.name(id,name)
                    case 2:
                        age =  int (input("Enter new age :"))
                        u1.age(id,age)
                    case 3:
                        grade =  input("Enter new grade :")
                        u1.grade(id,grade)
                    case 4:
                        email = input("Enter new email :")
                        u1.email(id,email)
                    case 5:
                        break
                    case _:
                        print("❌ !! Invalid Choice !! ❌")
        case 3:
            # ID to delete data
            id = int(input("Enter student id to delete :"))
            
            # Deleting data
            delete_student(id)
        case 4:
            f1 = search()
            
            # Searching Choices
            print("1. Find by id.")
            print("2. Find by name :")
            find_choice = int(input("Enter your choice :"))
            match find_choice:
                # inserting data to search 
                case 1:
                    id = int(input("Enter id to find :"))
                    f1.id(id)
                case 2:
                    name = input("Enter name to find :")
                    f1.name(name)
                case _:
                    print("❌ !! Invalid Choice !! ❌")
                    
        case 5:
            # Displaying all students data
            display_all()
            
        case 6:
            # Exiting application
            print("Thank You !")
            break
        case _:
            print("Invalid Choice !!")

cusor.close()
database.close()
