from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllSubject() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    closeConnection(conn)
    return subjects

def getSubjectbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM subjects WHERE sub_name = ?")
    cursor.execute(query, (name,))
    subject = cursor.fetchone()
    closeConnection(conn)
    return subject

def insertSubject(name) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO subjects (sub_id, sub_name) VALUES (NULL, ?)")
    data_subject = (name,)
    cursor.execute(add_query, data_subject)
    conn.commit()
    closeConnection(conn)
    return