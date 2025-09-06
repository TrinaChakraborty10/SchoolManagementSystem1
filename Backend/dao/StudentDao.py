from Backend.util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllStudents() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    closeConnection(conn)
    return students

def getStudentbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM students WHERE name = ?")
    cursor.execute(query, (name,))
    student = cursor.fetchone()
    closeConnection(conn)
    return student

def insertStudent(name, age, class_id) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO students (stud_id, name, dob, addr, class_id, school_id) VALUES (NULL, ?, NULL, NULL, ?, NULL)")
    data_student = (name, class_id)
    cursor.execute(add_query, data_student)
    conn.commit()
    closeConnection(conn)
    return
