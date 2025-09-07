from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllSchool() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schools")
    schools = cursor.fetchall()
    closeConnection(conn)
    return schools

def getSchoolbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM schools WHERE name = ?")
    cursor.execute(query, (name,))
    school = cursor.fetchone()
    closeConnection(conn)
    return school

def insertSchool(name, address) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO schools (name, address) VALUES (?, ?)")
    cursor.execute(add_query, (name, address))
    conn.commit()
    closeConnection(conn)
    return