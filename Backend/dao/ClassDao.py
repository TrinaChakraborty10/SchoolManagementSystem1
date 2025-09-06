from Backend.util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllClass() :
    # conn = sqlite3.connect('school.db')
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM class")
    classes = cursor.fetchall()
    closeConnection(conn)
    return classes

def getClassbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM class WHERE class_name = ?")
    cursor.execute(query, (name,))
    class_ = cursor.fetchone()
    closeConnection(conn)
    return class_

def insertClass(name, teacher) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO class (class_name) VALUES (?)")
    data_class = (name,)
    cursor.execute(add_query, data_class)
    conn.commit()
    closeConnection(conn)
    return