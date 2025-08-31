from dao import ClassDao

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
