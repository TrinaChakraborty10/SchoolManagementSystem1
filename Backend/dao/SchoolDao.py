from Backend.util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllSchool() :
    conn = getConnection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schools")
    schools = cursor.fetchall()
    conn.closeConnection()
    return schools

def getSchoolbyName(name):
    conn = getConnection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schools WHERE name = ?", (name,))
    school = cursor.fetchone()
    conn.closeConnection()
    return school

def insertSchool(name, address) :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO schools (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.closeConnection()
    return