import pymysql


def get_connection():
    # Creating connection to the database

    connection = pymysql.connect(
        host="localhost",
        user="root",          # Change if your MySQL username is different
        password="09202006",  # Replace with your MySQL password
        database="student_db"
    )
    return connection


def add_student(name, roll_no, course, email):
    # Inserting data into the database

    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO students (name, roll_no, course, email) VALUES(%s,%s,%s,%s)"
    
    # values = (name, roll_no, course, email)

    cursor.execute(query,(name,roll_no,course,email))
    connection.commit()

    cursor.close()
    connection.close()


def get_all_students():
    # Retrieving students data from the database

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students