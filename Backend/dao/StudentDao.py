from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllStudents() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    closeConnection(conn)
    return students

def getStudentbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM student WHERE name = ?")
    cursor.execute(query, (name,))
    student = cursor.fetchone()
    closeConnection(conn)
    return student

def insertStudent(name, age, address) :
    conn = getConnection()
    cursor = conn.cursor()
    print("Inserting student:", name, age, address)
    add_query = ("INSERT INTO student(name, age, addr) VALUES (%s, %s, %s)")
    data_student = (name, age, address)
    cursor.execute(add_query, data_student) 
    conn.commit()
    closeConnection(conn)
    return
