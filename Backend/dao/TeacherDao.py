from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllTeachers() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher")
    teacher = cursor.fetchall()
    closeConnection(conn)
    return teacher

def getTeacherbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM teacher WHERE name = %s")
    cursor.execute(query, (name,))
    teacher = cursor.fetchone()
    closeConnection(conn)
    return teacher

def insertTeacher(name, subject) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO teacher (name, subject) VALUES (%s, %s)")
    data_teacher = (name, subject)
    cursor.execute(add_query, data_teacher)
    conn.commit()
    closeConnection(conn)
    return