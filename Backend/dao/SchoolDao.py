from util.DButil import getConnection, closeConnection
# from ./util/DBUtil import getConnection, closeConnection
import sqlite3

def getAllSchool() :
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM school")
    schools = cursor.fetchall()
    closeConnection(conn)
    return schools

def getSchoolbyName(name):
    conn = getConnection()
    cursor = conn.cursor()
    query = ("SELECT * FROM school WHERE name = ?")
    cursor.execute(query, (name,))
    school = cursor.fetchone()
    closeConnection(conn)
    return school

def insertSchool(addr, board, coed, estd, medium, name) :
    conn = getConnection()
    cursor = conn.cursor()
    add_query = ("INSERT INTO school (addr, board, coed, estd, medium, name) VALUES (%s, %s, %s, %s, %s, %s)")
    cursor.execute(add_query, (addr, board, coed, estd, medium, name))
    conn.commit()
    print("Inserted school:", name)
    closeConnection(conn)
    return

def searchSchools(name=None, board=None):
    conn = getConnection()
    cursor = conn.cursor()
    query = "SELECT * FROM school WHERE 1=1"
    params = []   
    if name:
        query += " AND name = %s"
        params.append(name)
    if board:
        query += " AND board = %s"
        params.append(board)
    cursor.execute(query, tuple(params))
    schools = cursor.fetchall()
    closeConnection(conn)
    return schools

def countSchoolsByBoard(board):
    conn = getConnection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM school WHERE board = %s"
    cursor.execute(query, (board,))
    count = cursor.fetchone()[0]
    closeConnection(conn)
    return count