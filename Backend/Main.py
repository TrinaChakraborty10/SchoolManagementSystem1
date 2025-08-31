import mysql.connector
from util import DButil
from dao import ClassDao

# # Connect to server
# cnx = DButil.getConnection()

# # Get a cursor
# cur = cnx.cursor()

# # Execute a query
# cur.execute("SELECT school_id FROM sms.school")

# # Fetch one result
# row = cur.fetchone()
# print("Current date is: {0}".format(row[0]))

# # Close connection
# DButil.closeConnection()

# ClassDao.getAllClass()
# ClassDao.getClassbyName("10th Grade")
# ClassDao.insertClass("11th Grade", "Mr. Smith")
# ClassDao.getAllClass()

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/classes/")
def get_classes():
    classes = ClassDao.getAllClass()
    return {"classes": classes}

@app.get("/classes/{name}")
def get_class_by_name(name: str):
    class_ = ClassDao.getClassbyName(name)
    return {"class": class_}

@app.post("/classes/")
def create_class(name: str, teacher: str):
    ClassDao.insertClass(name, teacher)
    return {"message": "Class created successfully"}
