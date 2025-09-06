from Backend.util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllTeachers() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    closeConnection(conn)
    return teachers

def getTeacherbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM teachers WHERE name = ?")
    cursor.execute(query, (name,))
    teacher = cursor.fetchone()
    closeConnection(conn)
    return teacher

def insertTeacher(name) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO teachers (tch_id, name) VALUES (NULL, ?)")
    data_teacher = (name,)
    cursor.execute(add_query, data_teacher)
    conn.commit()
    closeConnection(conn)
    return