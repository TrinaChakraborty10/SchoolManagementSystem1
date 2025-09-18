from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllSubject() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject")
    subject = cursor.fetchall()
    closeConnection(conn)
    return subject

def getSubjectbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM subject WHERE sub_name = %s")
    cursor.execute(query, (name,))
    subject = cursor.fetchone()
    closeConnection(conn)
    return subject

def insertSubject(name) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO subject (sub_name) VALUES (%s)")
    data_subject = (name,)
    cursor.execute(add_query, data_subject)
    conn.commit()
    print("Inserted subject:", name)
    closeConnection(conn)
    return