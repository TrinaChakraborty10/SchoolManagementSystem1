from Backend.util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllClass() :
    # conn = sqlite3.connect('school.db')
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM class")
    classes = cursor.fetchall()
    closeConnection(con)
    return classes

def getClassbyName(name):
    con = getConnection()
    cursor = con.cursor()
    query = ("SELECT * FROM class WHERE class_name = ?")
    cursor.execute(query, (name,))
    class_ = cursor.fetchone()
    closeConnection(con)
    return class_

def insertClass(name, teacher) :
    con = getConnection()
    cursor = con.cursor()
    add_query = ("INSERT INTO class (class_name) VALUES (?)")
    data_class = (name,)
    cursor.execute(add_query, data_class)
    con.commit()
    closeConnection(con)
    return